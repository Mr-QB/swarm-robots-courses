# Mô phỏng thuật toán theo dõi đa mục tiêu (MTT) của hệ thống đa robot

## Giới thiệu

Chương trình này là một mô phỏng của thuật toán theo dõi đa mục tiêu (MTT) được triển khai cho một hệ thống đa robot. Thuật toán này giúp các robot trong hệ thống tìm và theo dõi nhiều mục tiêu cùng một lúc.

## Ý tưởng thuật toán

Thuật toán MTT trong chương trình này hoạt động theo các bước sau:

1. **Tìm kiếm mục tiêu**: Các robot di chuyển ngẫu nhiên sẽ tìm kiếm các mục tiêu trong môi trường xung quanh dựa trên phạm vi nhìn thấy.
2. **Phân công mục tiêu**: Khi một mục tiêu được phát hiện, các robot sẽ cạnh tranh để phân công mục tiêu cho mình. Một robot được chọn để theo dõi mỗi mục tiêu.
3. **Di chuyển đến mục tiêu**: Các robot sẽ di chuyển đến mục tiêu của mình bằng cách tính toán hướng di chuyển dựa trên vị trí của mục tiêu và tránh va chạm với các robot khác.
4. **Theo dõi mục tiêu**: Khi đến gần với mục tiêu, robot sẽ theo dõi mục tiêu đó và cập nhật trạng thái của mình.

Các trạng thái của **Target**:
1. `free`: Trạng thái mặc định khi một target mới được tạo ra và chưa được gán cho bất kỳ agent nào. Trong trạng thái này, target có thể được agent tìm kiếm và phân công.

2. `finded`: Khi một agent đã phát hiện target và quyết định theo dõi nó, trạng thái của target chuyển sang finded. Trong trạng thái này, target không còn tự do và đã được phân công cho một agent cụ thể.

3. `unfree`: Trạng thái này chỉ xuất hiện khi target đã được phân công cho một agent. Trong trạng thái này, target không còn tự do và đang được agent theo dõi.

Các trạng thái của **Agent**
1. unassigned: Trạng thái mặc định khi một agent mới được tạo ra và chưa được phân công cho bất kỳ target nào. Trong trạng thái này, agent có thể tìm kiếm (di chuyển trong map) và chờ phân công từ hệ thống.

2. assigned: Khi agent đã được phân công để theo dõi một target cụ thể, trạng thái của agent chuyển sang assigned. Trong trạng thái này, agent đang di chuyển đến target đã được phân công và cố gắng theo dõi nó.

3. occupied: Trạng thái này có thể áp dụng sau khi agent đã đến gần target và bắt đầu theo dõi nó. Trong trạng thái này, agent đã đạt được mục tiêu của mình và không còn thực hiện các hoạt động di chuyển tích cực nữa

## Một số hình ảnh demo
Dưới đây là một số hình ảnh demo của chương trình

![Demo](Demo/Multi-targetTrackingDemo.gif)