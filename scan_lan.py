import subprocess
import re
import socket
import concurrent.futures

def get_local_ip_base():
    """Lay dai mang LAN hien tai cua may tinh"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "192.168.1.1"
    finally:
        s.close()
    
    parts = local_ip.split(".")
    base = f"{parts[0]}.{parts[1]}.{parts[2]}"
    return base, local_ip

def ping_host(ip):
    """Ping nhe 1 goi tin de kich hoat bang ARP"""
    # Windows ping: -n 1 (1 goi), -w 300 (timeout 300ms)
    cmd = ["ping", "-n", "1", "-w", "300", ip]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return ip, res.returncode == 0

def scan_arp():
    """Doc bang ARP tren Windows de lay IP va MAC"""
    output = subprocess.check_output(["arp", "-a"], text=True)
    devices = []
    for line in output.splitlines():
        line = line.strip()
        match = re.search(r"(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F-]+)\s+(\w+)", line)
        if match:
            ip, mac, ip_type = match.groups()
            if ip_type.lower() == "dynamic" and not ip.endswith(".255"):
                devices.append({"ip": ip, "mac": mac})
    return devices

def main():
    base, local_ip = get_local_ip_base()
    print(f"[*] May hien tai: {local_ip}")
    print(f"[*] Dang quet nhanh dai mang {base}.1 -> {base}.254...")

    ips = [f"{base}.{i}" for i in range(1, 255)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        list(executor.map(ping_host, ips))

    devices = scan_arp()
    print("\n" + "="*60)
    print(f"{'IP Address':<18} | {'MAC Address':<20} | Hostname")
    print("="*60)

    for dev in sorted(devices, key=lambda x: [int(p) for p in x['ip'].split('.')]):
        try:
            hostname = socket.gethostbyaddr(dev['ip'])[0]
        except Exception:
            hostname = "(Chua ro ten)"
        print(f"{dev['ip']:<18} | {dev['mac']:<20} | {hostname}")

    print("="*60)
    print(f"[+] Phat hien tong cong {len(devices)} thiet bi dang online trong nha.")

if __name__ == "__main__":
    main()
