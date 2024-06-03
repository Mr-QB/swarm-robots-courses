# Giải quyết vấn đề người du lịch (TSP) bằng thuật toán tối ưu hóa của một đàn kiến (ACO)

## Giới thiệu
Trong các tình huống thực tế, vấn đề người du lịch (TSP) là một vấn đề tối ưu quan trọng và được nghiên cứu rộng rãi. ACO là một thuật toán metaheuristic dựa trên hành vi tự tổ chức của kiến và được sử dụng rộng rãi để giải quyết vấn đề này.

## Cài đặt
Mã trong tập tin [TSP_with_ACO.ipynb](TSP_with_ACO.ipynb) cung cấp một cài đặt đơn giản của thuật toán ACO để giải quyết TSP. Để chạy chương trình, bạn cần cài đặt Python cùng với các thư viện matplotlib và numpy. Bạn có thể cài đặt các thư viện bằng cách chạy lệnh sau:

```pip install matplotlib numpy```

## Sử dụng
1. Chỉnh sửa các tham số trong tệp [TSP_with_ACO.ipynb](TSP_with_ACO.ipynb) để đáp ứng yêu cầu của bài toán:
   - `num_cities`: Số lượng thành phố trong bài toán.
   - `num_ants`: Số lượng kiến (giải pháp) sẽ được thử.
   - `iterations`: Số lần lặp của thuật toán.
   - `alpha`: Hệ số Alpha, ảnh hưởng của mùi kiến trên việc chọn thành phố tiếp theo.
   - `beta`: Hệ số Beta, ảnh hưởng của khoảng cách đến thành phố tiếp theo.
   - `decay_factor`: Hệ số suy giảm, hệ số cho sự bay hơi của mùi sau mỗi lần lặp.
   - `Q`: Tham số Q, cần thiết để cập nhật ma trận mùi.

2. Chạy chương trình bằng cách thực thi các ô mã trong tệp [TSP_with_ACO.ipynb](TSP_with_ACO.ipynb).

## Kết quả
Sau khi chạy, chương trình sẽ hiển thị đường đi tốt nhất được tìm thấy bằng thuật toán ACO cùng với khoảng cách tương ứng.

## Mở rộng
Bạn có thể mở rộng chương trình bằng cách thử nghiệm với các tham số khác nhau, điều chỉnh thuật toán ACO, hoặc thêm các tính năng mới như các hiển thị trực quan phức tạp hơn.
