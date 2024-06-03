# Mô phỏng Định tuyến mạng bằng Pygame và thuật toán DSDV

Đây là một mô phỏng sử dụng Pygame để tạo ra một mạng của các node và định tuyến giữa chúng. Thuật toán Định tuyến DSDV (Destination-Sequenced Distance Vector Routing) được sử dụng để quản lý việc định tuyến trong mạng.

## Cách sử dụng

- Sử dụng chuột để di chuyển các node trên màn hình.
- Nhấn n để tạo một node mới.
- Nhấn chuột trái và kéo để di chuyển node.
- Các node sẽ tự động kết nối với nhau khi chúng gần nhau đủ.
- Bảng định tuyến của node sẽ hiển thị khi bạn nhấp vào một node.

## Thuật toán DSDV (Destination-Sequenced Distance Vector)

DSDV là một thuật toán định tuyến dựa trên vector khoảng cách với các phần tử trong bảng định tuyến được gửi theo chu kỳ hoặc khi có sự thay đổi trong mạng. Mỗi node trong mạng duy trì một bảng định tuyến, trong đó mỗi hàng chứa thông tin về một nút đích và khoảng cách đến nút đó.

DSDV sử dụng các số thứ tự địa chỉ để xác định các bản ghi mới và cũ trong bảng định tuyến. Khi một node thấy một thông điệp mới từ một node khác, nó sẽ cập nhật bảng định tuyến của mình với các thông tin mới và gửi thông điệp cập nhật đến các node khác.

## Demo
Một đoạn video demo ngắn của chương trình.

![Demo](Demo/DSDVDemo.gif)

