# Hệ Thống Giám Sát & Quản Lý Mạng Gia Đình (Home Network Monitor)

## 1. Phân Tích Hiện Trạng Nhà & Hạ Tầng Mạng

- **Diện tích**: 75m² (5m x 15m), nhà ống 4 tầng.
- **Vị trí thiết bị mạng**:
  - Tầng 1: Router chính (Modem nhà mạng hoặc Router riêng)
  - Tầng 2: Mesh Node 1
  - Tầng 3: **Trống (Không có Node)**
  - Tầng 4: Mesh Node 2
- **Thiết bị kết nối**:
  - Tầng 1: 1 Camera, 1 Robot hút bụi, 1 Smart TV
  - Tầng 2: 2 Camera, 2 Laptop, 1 Robot hút bụi
  - Tầng 3: 1 Camera, 1 Robot hút bụi (bắt sóng xuyên sàn từ T2 hoặc T4)
  - Tầng 4: 1 Camera, 1 Robot hút bụi
  - *Tổng cộng*: ~12 thiết bị cố định + điện thoại/tablet di động.

### ⚠️ Điểm yếu vật lý cần lưu ý:
1. **Tầng 3 là "vùng trũng" sóng**: Sàn bê tông cốt thép dày 10-15cm làm suy hao sóng 5GHz cực nặng (giảm 70-80%), sóng 2.4GHz xuyên qua được nhưng băng thông hẹp và dễ nghẽn khi robot/camera stream video.
2. **Backhaul giữa Node tầng 2 và Node tầng 4**:
   - Nếu **Mesh không dây (Wireless Backhaul)**: Node T4 phải bắt sóng của Node T2 qua 2 lớp sàn bê tông (sàn T3 và sàn T4). Tốc độ ở T4 sẽ bị suy giảm thê thảm (có thể chỉ còn 15-30% tốc độ gốc) và ping không ổn định.
   - **Khuyến nghị**: Nên đi 1 dây LAN âm tường/nẹp ngoài từ Tầng 1 lên T2, T3, T4 (Ethernet Backhaul) để toàn mạng đạt tốc độ tối đa.

---

## 2. Giải Pháp: Có Cần Tự Làm Không Hay Dùng GitHub?

**👉 KHÔNG CẦN VIẾT TỪ SỐ 0!** Trên GitHub đã có sẵn các dự án mã nguồn mở (Self-hosted) cực kỳ hoàn thiện, đẹp mắt và chạy mượt trên Docker (Windows / Linux / Mini PC / Laptop cũ):

| Nhu cầu | Tool GitHub khuyên dùng | Mục đích |
|---|---|---|
| **Đo tốc độ Internet tự động** | [alexjustesen/speedtest-tracker](https://github.com/alexjustesen/speedtest-tracker) | Tự động chạy Speedtest định kỳ (mỗi giờ/mỗi ngày), lưu lịch sử, vẽ biểu đồ Ping, Jitter, Download, Upload. |
| **Theo dõi Camera & Robot online/offline** | [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) | Ping kiểm tra tình trạng từng Camera, Robot, TV, Mesh Node. Gửi cảnh báo ngay về Telegram/Zalo nếu Camera bị rớt mạng. |
| **Quét toàn bộ thiết bị trong mạng (LAN Discovery)** | [netalertx/netalertx](https://github.com/netalertx/netalertx) | Tự động quét IP/MAC, lưu tên từng thiết bị, báo động khi có điện thoại lạ hoặc thiết bị lạ kết nối vào Wi-Fi. |
| **Kiểm tra tốc độ nội bộ giữa các tầng** | `iPerf3` / [LibreSpeed](https://github.com/librespeed/speedtest) | Đo tốc độ thực tế từ Laptop tầng 3 tới Router tầng 1 để biết tầng 3 bị nghẽn sóng ở mức nào. |
| **Quản lý bảo mật & Lưu lượng DNS** | [AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) | Chặn quảng cáo toàn mạng, xem thiết bị nào (camera Tàu, robot) đang gửi dữ liệu lạ ra internet. |

---

## 3. Cách Triển Khai Nhanh Bằng Docker Compose

Chỉ cần cài Docker Desktop trên Windows (hoặc trên 1 máy tính để bàn/laptop luôn bật), sau đó chạy:

```bash
docker compose up -d
```
