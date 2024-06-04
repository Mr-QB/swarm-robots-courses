# Kích thước cửa sổ
window_width = 800
window_height = 600

# Kích thước ô
cell_size = 20

# Màu sắc
WHITE = (255, 255, 255)  # Màu trắng
RED = (255, 0, 0)  # Màu đỏ
BLACK = (0, 0, 0)  # Màu đen
GREEN = (0, 255, 0)  # Màu xanh lá cây
YELLOW = (255, 255, 0)  # Màu vàng
BLUE = (0, 0, 255)  # Màu xanh dương

# Hệ số meter / pixel
# 1 pixel = 30cm
meter_pixel = 3 / 100

# Định nghĩa dải màu gradient
colors = ["blue", "green", "yellow", "red"]

last_rate = 0  # Tỉ lệ tốt nhất của ô lưới được phủ sóng, khởi tạo ban đầu là 0.
NUM_AP = 4  # Số lượng điểm truy cập (AP) trong mạng, trong trường hợp này là 3.
w = 0.9  # Hệ số trọng số cho vận tốc của agent trong thuật toán PSO.
c1 = 2.5  # Hệ số cho yếu tố cá nhân tốt nhất trong thuật toán PSO.
c2 = 0.8  # Hệ số cho yếu tố toàn cục tốt nhất trong thuật toán PSO.
agent_spacing = 50  # Khoảng cách giữa các agent
