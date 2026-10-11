# 🚗 Hệ thống đếm xe qua camera sử dụng YOLO pretrained

> Bài tập lớn – Trường Đại học Thăng Long – Chuyên ngành Trí tuệ nhân tạo

Hệ thống đếm phương tiện giao thông (xe máy, ô tô, xe tải/xe buýt) theo thời gian thực từ luồng camera giám sát. Dự án không chỉ dừng ở việc train một mô hình AI mà hướng tới một **hệ thống MLOps**: tự động hóa kiểm thử, giám sát sức khỏe mô hình và triển khai không gián đoạn.

## 👥 Nhóm thực hiện

| Thành viên | Vai trò | Nhiệm vụ chính |
| --- | --- | --- |
| Lê Nguyễn Nhật Huy | Trưởng nhóm, quản lý repo, Monitor | Prometheus + Grafana + cảnh báo, quản lý repository, viết báo cáo |
| Nguyễn Hồng Sơn | AI Engineer | Fine-tune YOLO pretrained, tích hợp DeepSORT, tối ưu tốc độ mô hình |
| Lê Quang Khải | Backend | Bọc module bằng FastAPI, xử lý đọc luồng video, cung cấp RESTful endpoint |
| Huỳnh Hải Nam | MLOps | Đóng gói ứng dụng (Docker), CI/CD trên GitHub, Nginx Canary Deployment |

## 🎯 Đối tượng phục vụ

- **Cán bộ quản lý, điều hành giao thông:** xem biểu đồ đếm xe, cảnh báo kẹt xe, xuất báo cáo lưu lượng theo ngày/tháng.
- **Nhân viên vận hành:** duy trì hệ thống, theo dõi phân tải, độ trễ và số khung hình/giây (FPS).

## 📦 Phạm vi sản phẩm

- Nhận diện và phân loại 3 nhóm phương tiện: **Xe máy**, **Ô tô con**, **Xe tải/Xe buýt**.
- Đếm lưu lượng dựa trên **vạch ảo**.
- Xây dựng luồng **CI/CD trên GitHub**.
- Phân luồng traffic bằng **Nginx** (Canary Deployment).
- Giám sát hiệu năng và độ trễ của model.

## ✨ Tính năng

| Tính năng | Mô tả |
| --- | --- |
| Nhận diện phương tiện | YOLO pretrained, lọc các class `car`, `motorcycle`, `bus`, `truck` |
| Theo dõi & gán ID | DeepSORT gán một ID duy nhất cho mỗi phương tiện |
| Logic đếm | Một hoặc nhiều vạch ảo; khi tâm bounding box cắt vạch thì biến đếm của nhãn đó tăng 1 |
| Xử lý video | Đọc file `.mp4` (test) và luồng RTSP (thực tế); dùng Queue/Threading của OpenCV để việc đọc không làm nghẽn nhận diện |
| RESTful API | Endpoint cho Frontend/Admin thao tác |
| Canary Deployment | Nginx chia traffic giữa model cũ và model mới theo tỷ lệ cấu hình được |
| Giám sát | Prometheus thu thập số liệu realtime, Grafana vẽ dashboard |

## 🔄 Luồng hoạt động

1. Hệ thống đọc luồng từ IP Camera hoặc file `.mp4`, đưa khung hình vào hàng đợi.
2. Khung hình lần lượt qua mô hình YOLO, trả về tọa độ bounding box và nhãn phân loại.
3. DeepSORT nhận kết quả và gán ID cho từng đối tượng.
4. Hệ thống kiểm tra tọa độ tâm của từng ID qua các khung hình; nếu cắt vạch ảo, biến đếm của nhãn tương ứng tăng 1.
5. Kết quả được lưu lại, Grafana vẽ lại biểu đồ mật độ giao thông.

Sơ đồ chi tiết: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## 🧱 Công nghệ

`Python` · `YOLO` · `DeepSORT` · `OpenCV` · `FastAPI` · `Docker` · `GitHub Actions` · `Nginx` · `Prometheus` · `Grafana`

## 📁 Cấu trúc repository

```
.
├── .github/
│   ├── workflows/ci.yml          # CI: lint + test + build image
│   └── pull_request_template.md
├── configs/                      # Cấu hình vạch ảo, nguồn video, ngưỡng...
├── data/                         # Dữ liệu mẫu (không commit file nặng)
├── docs/
│   └── ARCHITECTURE.md           # Kiến trúc hệ thống
├── models/                       # Trọng số model (không commit file nặng)
├── monitoring/
│   └── prometheus.yml
├── nginx/
│   └── nginx.conf                # Canary: chia traffic v1/v2
├── src/app/                      # Mã nguồn FastAPI + pipeline
├── tests/
├── Dockerfile
├── docker-compose.yml
├── GIT_WORKFLOW.md               # Quy trình Git của nhóm
└── requirements.txt
```

## 🚀 Chạy thử

```bash
git clone https://github.com/<ten-nhom>/vehicle-counting-mlops.git
cd vehicle-counting-mlops

# Chạy riêng API
pip install -r requirements.txt
uvicorn src.app.main:app --reload

# Hoặc chạy toàn bộ hệ thống (API v1/v2 + Nginx + Prometheus + Grafana)
docker compose up --build
```

| Dịch vụ | Địa chỉ |
| --- | --- |
| API (qua Nginx) | http://localhost:8080 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

## 🌿 Quy trình Git

Nhóm làm việc theo mô hình nhánh `main` / `develop` / `feature/*` kèm Pull Request và review chéo. Xem [GIT_WORKFLOW.md](GIT_WORKFLOW.md).

## 📌 Tiến độ

- [ ] Fine-tune YOLO và tích hợp DeepSORT
- [ ] Logic đếm bằng vạch ảo
- [ ] FastAPI + đọc luồng video (mp4/RTSP)
- [ ] Đóng gói Docker
- [ ] CI/CD trên GitHub Actions
- [ ] Nginx Canary Deployment
- [ ] Prometheus + Grafana + cảnh báo
- [ ] Báo cáo

> Ghi chú: các thư mục và file cấu hình trong repo hiện là khung ban đầu; từng thành viên hoàn thiện phần của mình theo bảng phân công.
