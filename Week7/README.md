# Phỏng Điều Khiển Bao Phủ Đa Robot Trong Môi Trường Có Cấu Trúc Bất Kỳ

## Giới thiệu
Chương trình mô phỏng này mô tả quá trình điều khiển bao phủ đa robot trong một môi trường có cấu trúc bất kỳ. Trong môi trường này, các robot cần phải tìm cách chiếm đóng các điểm trên bản đồ một cách hiệu quả để bảo vệ và giám sát các khu vực quan trọng.

## Thuật Toán
Các robot trong môi trường này sẽ hoạt động theo các trạng thái sau:
- **"Đã Chiếm Đóng"**: Robot đứng yên tại một điểm đã chiếm đóng và tạo các điểm ảo xung quanh để truyền thông tin.
- **"Được Phân Công"**: Robot được phân công đi tới một điểm ảo và sử dụng thuật toán di chuyển và tránh vật cản để đến đó.
- **"Chưa Được Phân Công"**: Robot chưa được phân công đi tới bất kỳ điểm nào và đứng yên tại vị trí ban đầu.

Quá trình hoạt động của thuật toán bao gồm:
1. Khởi tạo môi trường với các điểm và vật cản ngẫu nhiên.
2. Khởi tạo các robot và bắt đầu chúng từ trạng thái "Chưa Được Phân Công".
3. Khi một điểm ảo trên bản đồ không được chiếm đóng, một robot sẽ được phân công để đi tới và chiếm đóng nó.
4. Robot di chuyển đến điểm ảo được chỉ định bằng thuật toán di chuyển và tránh vật cản.
5. Khi robot đạt được điểm ảo, nó chuyển sang trạng thái "Đã Chiếm Đóng" và bắt đầu tạo các điểm ảo mới xung quanh vị trí hiện tại.
6. Quá trình tiếp tục cho đến khi tất cả các điểm trên bản đồ được chiếm đóng hoặc chương trình kết thúc.

## Giải Thích Mã

Trong chương trình này, các tệp Python chính bao gồm `agent.py`, `main.py`, `setting.py`, và `supportfunction.py`. Dưới đây là chức năng chính của mỗi tệp:

### Tệp `agent.py`
Định nghĩa lớp `Agent` đại diện cho các robot trong môi trường. Cung cấp các phương thức để vẽ, di chuyển, và tránh vật cản cho mỗi robot.
### Tệp `main.py`
Thực hiện vòng lặp chính của chương trình, trong đó điều khiển việc di chuyển của các robot, xử lý va chạm, và vẽ trạng thái mới lên màn hình.
### Tệp `setting.py`
Chứa các thiết lập và tham số cố định cho chương trình như kích thước cửa sổ, màu sắc, và các thông số vận tốc, phạm vi tránh vật cản của các robot.
### Tệp `supportfunction.py`
Chứa các hàm hỗ trợ như tính toán khoảng cách giữa các điểm, phép cộng mảng, và tìm kiếm cột trong mảng 2D.


## Chạy Chương Trình
Để chạy chương trình, bạn cần cài đặt các thư viện cần thiết, chỉnh sửa các tham số trong `Setting.py` và sau đó chạy file `main.py`.

Trong chương trình, bạn có thể ấn:
 * Phím **S** để bắt đầu trình mô phỏng
 * Phím **Esc** để thoát khỏi chương trình

## Một số hình ảnh demo
Dưới đây là một số hình ảnh demo của chương trình

![Demo](Demo/Occupythemulti-robotarea.gif)
