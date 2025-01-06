# BTL-DSA-Bloom-Filter

## Mô Tả Dự Án

Dự án **BTL-DSA-Bloom-Filter** triển khai một Bloom Filter bằng Python để kiểm tra sự hiện diện của các URL trong danh sách Phishing. Dự án bao gồm việc tải danh sách Phishing URLs từ file CSV, thêm chúng vào Bloom Filter, và thực hiện kiểm tra với một tập hợp các URL ngẫu nhiên để tính toán tỷ lệ dương tính giả (False Positive Rate). Kết quả được biểu diễn qua đồ thị để dễ dàng so sánh với ngưỡng p = 0.05.

## Yêu Cầu
- **Thư viện Python:**
  - `csv`
  - `matplotlib`
  - `random`
  - `mmh3`
  - `bitarray`

## Cài Đặt

### 1. Tải Repo Về

Trước tiên, bạn cần tải repository về máy tính của mình. Bạn có thể làm điều này bằng cách sử dụng `git`:

```bash
git clone https://github.com/Ben-cp/BTL-DSA-Bloom-Filter-.git
