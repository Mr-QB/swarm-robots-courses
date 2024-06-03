# Flocking Reynolds

## Giới thiệu

Kho lưu trữ này chứa mã nguồn Python cho một bài toán mô phỏng về Flocking Reynolds, một thuật toán mô phỏng hành vi đàn bầy trong lập trình máy tính đồ hoạ. Thuật toán này được lấy cảm hứng từ nghiên cứu của Craig Reynolds về hành vi đàn bầy trong tự nhiên.

Các mã chương trình được tham khảo từ kho lưu trữ simple-Flocking-simulation-python-pygame của [Josephbakulikira](https://github.com/Josephbakulikira)

## Các Tính Năng Chính

### 1. Boid (vật chứa):
Mỗi boid được mô hình hóa như một cá thể có khả năng di chuyển độc lập và tương tác với các boid khác trong đàn.
  
### 2. Hành Vi Đàn Bầy:
 Boid thực hiện ba hành vi cơ bản của đàn bầy: tách biệt (separation), căn chỉnh (alignment) và đồng lòng (cohesion). Các hành vi này giúp boid duy trì khoảng cách an toàn, đi theo hướng chung và di chuyển về phía trung tâm của đàn.

#### 2.1 Tách Biệt (Separation)

Hành vi tách biệt giúp boid tránh va chạm và duy trì một khoảng cách an toàn với các boid xung quanh. Boid sẽ cảm nhận và phản ứng khi có boid khác nằm trong phạm vi nhất định (radius) xung quanh nó. Khi đó, nó sẽ cố gắng di chuyển ra xa boid đó để tránh va chạm.

Công thức tính lực tách biệt: 

<img src="https://latex.codecogs.com/svg.image?&space;Steering=\frac{\sum_{j}^{}(position_{self}-position_{mate})}{distance_{mate}^2}" title="Separation" />

Trong đó:
 * **Steering** là vector biểu thị hướng và lực tách biệt.
 * **position_self** là vị trí của boid hiện tại.
 * **position_mate** là vị trí của boid hàng xóm.
 * **distance_mate** là khoảng cách giữa boid hiện tại và boid hàng xóm.
 
#### 2.2 Đồng Lòng (Cohesion)

Hành vi đồng lòng là sự hướng về phía trung tâm của các boid xung quanh. Boid cảm nhận vị trí của các boid khác trong phạm vi nhất định và cố gắng di chuyển về phía trung tâm của chúng. Điều này giúp duy trì độ gần gũi và tự tổ chức trong đàn.

Công thức tính lực đồng lòng: 

<img src="https://latex.codecogs.com/svg.image?&space;Steering=\frac{\sum_j&space;position_{mate}}{n}-position_{self}" title="Cohesion" />

Trong đó: 
 * **Steering** là vector biểu thị hướng và lực đồng lòng.
 * **position_self** là vị trí boid hiện tại.
 * **Position_mate** là vị trí boid hàng xóm.
 * **n** là số lượng boid trong đàn.

#### 2.3 Căn Chỉnh (Alignment)

Hành vi căn chỉnh đảm bảo rằng boid di chuyển theo hướng chung của các boid xung quanh. Boid cảm nhận hướng di chuyển của các boid trong phạm vi nhất định và cố gắng đi theo hướng đó. Điều này giúp đàn bầy di chuyển một cách đồng đều và có tổ chức.

Công thức tính lực căn chỉnh: 

<img src="https://latex.codecogs.com/svg.image?&space;Steering=\frac{\sum_j&space;velocity_{mate}}{n}-velocity_{self}" title="Alignment" />

Trong đó:
 * **Steering** là vector biểu thị hướng và lực căn chỉnh.
 * **velocity_self** là vận tốc của boid hiện tại.
 * **velocity_mate** là vận tốc của boid hàng xóm.
 * **n** là số lượng boid trong đàn.

### Mô Phỏng 3D: 
Boid được mô phỏng trong không gian ba chiều với hình dạng và hành vi động động phù hợp.

## Cách Sử Dụng
#### Chạy Mã Nguồn:
Chạy chương trình Python để mô phỏng hành vi đàn bầy. Có thể tinh chỉnh các thông số và hành vi trong mã nguồn để thí nghiệm và tùy chỉnh theo nhu cầu.
#### Thao tác với công cụ:
 * `U` để chuyển đổi bảng giao diện người dùng
 * `R` để đặt lại (Reset)
 * `ESC` để thoát mô phỏng

## Demo chương trình
Dưới đây là đoạn mã Python để hiển thị một video demo về hành vi đàn bầy của boids:

![2_agent_demo](demo\demo.gif)

