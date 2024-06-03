from supportFunction import *  # Import các hàm hỗ trợ từ file supportFunction.py
from Agent import Agent  # Import lớp Agent từ file Agent.py


# Tạo cửa sổ và subplot
fig, ax = plt.subplots()
ax.set_title("Window")
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])

# Vẽ lưới
draw_grid(ax)

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
image = imread("Input\house_cad.png")
plt.imshow(image)
# plt.grid(True)
for agent in agents:
    # Vòng lặp duyệt qua tất cả các agent trong danh sách agents
    # Mỗi agent đại diện cho một điểm truy cập (AP) trong mạng.

    # Khởi tạo biến đếm số ô lưới không được phủ sóng đủ mạnh
    cell_uncovered_count = 0

    for center in cell_centers:
        # Duyệt qua tất cả các tâm của các ô lưới trong không gian mạng

        # Khởi tạo biến lưu khoảng cách tới điểm truy cập gần nhất
        closest_ap_distance = 9999

        for ap_loc in agents:
            # Duyệt qua tất cả các agent để tính khoảng cách từ mỗi ô lưới tới các điểm truy cập

            # Tính khoảng cách từ ô lưới đến điểm truy cập hiện tại
            distance_to_ap = (
                math.sqrt((ap_loc.x - center[0]) ** 2 + (ap_loc.y - center[1]) ** 2)
                * meter_pixel
            )

            # Cập nhật khoảng cách tới điểm truy cập gần nhất
            if distance_to_ap <= closest_ap_distance:
                closest_ap_distance = distance_to_ap

            # Tính toán tín hiệu dựa trên khoảng cách và chuyển đổi thành màu sắc tương ứng
            signal = signalCalculation(closest_ap_distance)
            color = dBm_to_color(signal)

            # Tăng biến đếm nếu tín hiệu không đủ mạnh
            if signal <= -60:
                cell_uncovered_count += 1

            # Vẽ ô lưới với màu sắc tương ứng
            ax.add_patch(
                plt.Rectangle(
                    (
                        center[0] - cell_size // 2,
                        center[1] - cell_size // 2,
                    ),  # Vị trí bắt đầu của ô lưới
                    cell_size,  # Chiều rộng của ô lưới
                    cell_size,  # Chiều cao của ô lưới
                    color=color,  # Màu sắc của ô lưới dựa trên tín hiệu
                )
            )

    # Tính tỷ lệ ô lưới được phủ sóng đủ mạnh
    current_rate = (num_cell - cell_uncovered_count) / num_cell * 100

    # Cập nhật điểm tốt nhất nếu cần thiết
    if current_rate >= last_rate:
        agent.pbest_rate = current_rate
        last_rate = current_rate
        agent.pbest_x = agent.x
        agent.pbest_y = agent.y
    if current_rate > biggest_rate:
        gbest_x = agent.x
        gbest_y = agent.y
        biggest_rate = current_rate

# In ra tỷ lệ ô lưới được phủ sóng tốt nhất
print("Best covered rate: " + str(biggest_rate) + "  " + str(count))

# Hiển thị kết quả
# if biggest_rate > 95:
plt.show()
