# Mô phỏng đội hình bay V-shaped bằng Pygame

## Thuật toán

1. **Khởi tạo**: Bắt đầu bằng việc tạo một số lượng agents (đối tượng) để đại diện cho các máy bay trong đội hình. Các agents sẽ được đặt ở một vị trí ban đầu và có một hướng bay cố định ban đầu.

2. **Tạo hình dáng V-shaped**: Các agents sẽ được tổ chức theo hình dáng V-shaped, với một agent ở trung tâm và các agent khác sẽ bay ở hai bên theo hình dáng hình chữ V.

3. **Phản ứng với sự di chuyển của chuột**: Khi di chuyển chuột, các agents sẽ thay đổi hướng bay của mình để đi theo hướng mà chuột di chuyển. Điều này có thể được thực hiện bằng cách tính toán góc giữa vị trí hiện tại của chuột và vị trí của mỗi agent, sau đó cập nhật hướng bay của từng agent.

4. **Vẽ mô phỏng**: Sử dụng thư viện Pygame để vẽ mô phỏng, hiển thị các agents và hình dáng của đội hình V-shaped lên màn hình.

5. **Cập nhật liên tục**: Liên tục cập nhật vị trí và hướng bay của các agents để duy trì hình dáng V-shaped và phản ứng với sự di chuyển của chuột.

## Demo
Dưới đây là một số hình ảnh về chương trình mô phỏng
![2_agent_demo](demo\V-ShapeFormation.gif)

## Kết luận
Thuật toán đơn giản này mô phỏng việc tổ chức và điều chỉnh đội hình bay theo hình dáng V-shaped bằng cách sử dụng Pygame. Mặc dù đơn giản, nó cung cấp một cái nhìn tổng quan về cách tổ chức đội hình bay và là một bước khởi đầu để tìm hiểu sâu hơn về các phương pháp tối ưu hóa hiệu suất bay.
