# Mô phỏng kiến trúc phản ứng sử dụng mạng nơ ron nhân tạo cho robot e-puck

## Giới thiệu
Báo cáo này tập trung vào việc nghiên cứu và mô phỏng việc áp dụng mạng nơ ron nhân tạo trong điều khiển robot e-puck.

## Lý thuyết
Trong thử nghiệm này, chúng tôi sử dụng mạng nơ ron nhân tạo như một bộ não ảo cho robot e-puck. Dữ liệu từ các cảm biến như cảm biến tiếp xúc, cảm biến khoảng cách và cảm biến màu sắc được thu thập và đưa vào mạng nơ ron. Mạng nơ ron sau đó phản hồi bằng cách tạo ra các quyết định về hành động tiếp theo của robot dựa trên thông tin đầu vào từ môi trường.

Bạn có thể xem mã của chương trình tại đây: [responseUsingNeuralNetworks\controllers\AnnControl\AnnControl.py](responseUsingNeuralNetworks\controllers\AnnControl\AnnControl.py)

Trong chương trình này, chúng tôi đã chọn một kiến trúc mạng nơ ron đơn giản nhưng hiệu quả. Mạng này bao gồm các lớp nơ ron kết nối đầy đủ và được kích hoạt bằng hàm sigmoid. Để tăng tính linh hoạt và khả năng học của mạng, chúng tôi đã áp dụng một ma trận tỷ lệ nhất định. Dưới đây là phần mã mô tả ma trận :

```python
self.scale_matrix = [[-0.2, 0.2], [-0.1, 0.1], [-0.05, 0.05], [-0.05, 0.05], [0.05, -0.05], [0.05, -0.05], [0.1, -0.1], [0.2, -0.2]]
```
## Một số hình ảnh demo
Dưới đây là một số hình ảnh của chương trình mô phỏng với mã được đề xuất:
![VideoDemo](Demo\AnnDemo.gif)
