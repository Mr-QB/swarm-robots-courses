import matplotlib.pyplot as plt
import cv2
from matplotlib.image import imread
from supportFunction import *  # Import các hàm hỗ trợ từ file supportFunction.py
from Agent import Agent  # Import lớp Agent từ file Agent.py

last_rate = 0
NUM_AP = 3
w = 0.9
c1 = 1
c2 = 1

# Khởi tạo agent
agents = [
    Agent(np.random.randint(0, window_width), np.random.randint(0, window_height), 0)
    for _ in range(NUM_AP)
]
cell_centers = calculate_cell_centers()
num_cell = len(cell_centers)
gbest_x = window_width / 2
gbest_y = window_height / 2
biggest_rate = 0
count = 0
# Đọc bức ảnh từ tệp
image = cv2.imread("Input\house_cad.png")
# image = imread("Input\house_cad.png")
for agent in agents:
    # Vòng lặp duyệt qua tất cả các agent trong danh sách agents
    # Mỗi agent đại diện cho một điểm truy cập (AP) trong mạng.

    # Khởi tạo biến đếm số ô lưới không được phủ sóng đủ mạnh
    cell_uncovered_count = 0


# Hiển thị bức ảnh
plt.imshow(image)
plt.grid(True)
plt.show()
