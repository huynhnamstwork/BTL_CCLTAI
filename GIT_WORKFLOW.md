# Quy trình Git của nhóm

## 1. Cấu trúc nhánh

| Nhánh | Mục đích |
| --- | --- |
| `main` | Code ổn định, chạy được. **Không commit trực tiếp.** |
| `develop` | Nhánh tích hợp, gộp các tính năng trước khi lên `main` |
| `feature/<ten>` | Mỗi người, mỗi tính năng một nhánh |
| `fix/<ten>` | Sửa lỗi |

Ví dụ: `feature/yolo-finetune`, `feature/deepsort-tracking`, `feature/fastapi-endpoints`, `feature/nginx-canary`, `feature/grafana-dashboard`.

## 2. Các bước làm việc

```bash
git checkout develop
git pull
git checkout -b feature/ten-tinh-nang

# ... code ...

git add <file>
git commit -m "feat: mô tả ngắn"
git push -u origin feature/ten-tinh-nang
```

Sau đó tạo **Pull Request** vào `develop`.

## 3. Pull Request và review

- Mỗi PR cần ít nhất **1 thành viên khác** review và duyệt.
- CI (GitHub Actions) phải chạy xanh trước khi merge.
- Merge xong thì xóa nhánh feature.
- Trưởng nhóm gộp `develop` vào `main` khi hoàn thành mỗi mốc.

## 4. Quy ước commit message

| Tiền tố | Ý nghĩa |
| --- | --- |
| `feat:` | Thêm tính năng |
| `fix:` | Sửa lỗi |
| `docs:` | Sửa tài liệu |
| `refactor:` | Chỉnh code, không đổi chức năng |
| `test:` | Thêm/sửa test |
| `ci:` | Sửa CI/CD, Docker, Nginx |

## 5. Phân công review 

| Người viết | Người review |
| --- | --- |
| Sơn (AI) | Khải (Backend) |
| Khải (Backend) | Nam (MLOps) |
| Nam (MLOps) | Huy (Monitor) |
| Huy (Monitor) | Sơn (AI) |

## 6. Xử lý conflict

```bash
git checkout feature/ten-tinh-nang
git pull origin develop      # kéo develop về nhánh mình
# mở file conflict, chọn đoạn đúng, bỏ dấu <<<<<<< ======= >>>>>>>
git add <file>
git commit
git push
```

## 7. Không commit

Dữ liệu video nặng, trọng số model lớn (`*.pt`), file `.env`, API key. Đã có trong `.gitignore`.
