# Home Network Monitor 🌐

Ứng dụng giám sát và kiểm tra sức khỏe hệ thống mạng gia đình / văn phòng cục bộ (Local Network Monitor & Speedtest). 

Ứng dụng được thiết kế tối ưu cho **macOS (Apple Silicon M1/M2/M3)** và có thể chạy trên mọi nền tảng hỗ trợ Python / Docker.

---

## 🚀 Tính Năng Chính

* 🔍 **Tự Động Quét Thiết Bị Mạng LAN (Auto Network Discovery)**:
  * Tự động dò quét toàn bộ dải mạng LAN qua ARP và Ping sweep.
  * Tự động phát hiện thiết bị mới kết nối vào Wi-Fi (Camera, Robot hút bụi, Smart TV, Laptop, Điện thoại...) mà không cần nhập tay.
* ⚡ **Kiểm Tra Trạng Thái & Độ Trễ (Live Latency & Health Check)**:
  * Ping đồng thời tất cả thiết bị trong mạng, đo độ trễ (latency ms) và tỷ lệ rớt gói tin (packet loss).
  * Phát hiện ngay thiết bị nào đang bị chập chờn hoặc rớt mạng.
* 📶 **Soi Sóng Wi-Fi MacBook (Wi-Fi Inspector)**:
  * Đọc cường độ sóng Wi-Fi (RSSI dBm), kênh tần số (2.4GHz / 5GHz), BSSID và tốc độ kết nối (Tx Rate).
  * Hữu ích khi di chuyển giữa các phòng / tầng để tìm điểm chết sóng Wi-Fi.
* 🚀 **Đo Tốc Độ Internet Tích Hợp (1-Click Speedtest)**:
  * Kiểm tra nhanh tốc độ Download, Upload và Ping thực tế của đường truyền.
* 🔒 **Bảo Mật & Riêng Tư Tuyệt Đối**:
  * 100% dữ liệu xử lý cục bộ trên máy, không gửi thông tin ra máy chủ ngoài.

---

## 📥 Tải Về & Cài Đặt

### 1. Dành cho macOS (Apple Silicon M1/M2/M3)
* Tải bản đóng gói sẵn tại mục [Releases](https://github.com/vnnit/home-network-monitor/releases).
* Tải file `HomeNetworkMonitor-macOS-AppleSilicon.zip`, giải nén và mở file `HomeNetworkMonitor.app`.
* *(Lưu ý lần đầu: Chuột phải vào app > chọn Open)*.

### 2. Chạy Trực Tiếp Bằng Python
Yêu cầu Python 3.9 trở lên:
```bash
# Clone source code
git clone https://github.com/vnnit/home-network-monitor.git
cd home-network-monitor

# Cài đặt thư viện (nếu cần giao diện app cửa sổ native)
pip install -r requirements.txt

# Khởi chạy
python app.py
```
App sẽ tự động mở giao diện Dashboard tại địa chỉ `http://127.0.0.1:8765`.

### 3. Triển Khai Docker (Tùy Chọn Chạy 24/7 Trên Server/NAS)
Nếu bạn muốn dựng server giám sát liên tục 24/7 trên Mini PC, NAS hoặc Docker:
```bash
docker compose up -d
```

---

## 🛠️ Công Nghệ Sử Dụng

* **Core**: Python (Standard Library HTTP Server, ARP Scanning, Multi-threading)
* **Frontend**: HTML5, Tailwind CSS, FontAwesome, WebKit
* **Build System**: GitHub Actions (Runner macOS-14 Apple Silicon)
