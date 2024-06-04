from supportFunction import *  # Import các hàm hỗ trợ từ file supportFunction.py
from Agent import Agent  # Import lớp Agent từ file Agent.py
import imageio  # Thêm thư viện để tạo và lưu file GIF từ các hình ảnh đầu ra.

# Tạo cửa sổ và subplot
fig, ax = plt.subplots()
ax.set_title("Window")
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])

# Vẽ lưới
drawGrid(ax)  # Gọi hàm drawGrid để vẽ lưới lên subplot.

# Khởi tạo agent
agents = [
    Agent(i * agent_spacing, j * agent_spacing, 0)
    for i in range(1, NUM_AP + 1)
    for j in range(1, NUM_AP + 1)
]

cell_centers = (
    calculateCellCenters()
)  # Tính toán và lưu trữ tọa độ trung tâm của các ô lưới.
num_cell = len(cell_centers)  # Số lượng ô lưới trong không gian mạng.
gbest_x = (
    window_width / 2
)  # Tọa độ x của điểm tốt nhất (GBest), khởi tạo ở giữa cửa sổ.
gbest_y = (
    window_height / 2
)  # Tọa độ y của điểm tốt nhất (GBest), khởi tạo ở giữa cửa sổ.
# Tỉ lệ tốt nhất của ô lưới được phủ sóng, khởi tạo ban đầu là 0.
biggest_rate = 0
count = 0  # Biến đếm số lần lặp.
image = imread("Week8\Input\house_cad.png")  # Đọc hình ảnh từ file cad ngôi nhà.
plt.imshow(image)  # Hiển thị hình ảnh nền.
loop = True  # Biến kiểm soát vòng lặp chính của chương trình.

stale_count = 0  # Biến đếm số lần lặp mà biến biggest_rate không thay đổi.
biggest_rate_l = 0  # Biến lưu trữ biggest_rate của lần lặp trước để so sánh.

while loop:
    ax.clear()  # Xóa hình ảnh trên subplot.
    ax.imshow(image, extent=[0, window_width, 0, window_height])  # Hiển thị hình ảnh nền.
    for ap_loc in agents:  # Duyệt qua từng agent trong danh sách các agent.
        cell_uncovered_count = 0
        for center in cell_centers:  # Duyệt qua từng tâm của các ô lưới trong không gian mạng.
            closest_ap_distance = 9999
            distance_to_ap = (
                math.sqrt((ap_loc.x - center[0]) ** 2 + (ap_loc.y - center[1]) ** 2)
                * meter_pixel
            )

            # Cập nhật khoảng cách tới điểm truy cập gần nhất
            if distance_to_ap <= closest_ap_distance:
                closest_ap_distance = distance_to_ap

            # Tính toán tín hiệu dựa trên khoảng cách và chuyển đổi thành màu sắc tương ứng
            signal = signalCalculation(closest_ap_distance)
            color = dBmToColor(signal)

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

        if current_rate >= ap_loc.pbest_rate:
            ap_loc.pbest_rate = current_rate
            ap_loc.pbest_x = ap_loc.x
            ap_loc.pbest_y = ap_loc.y
        if current_rate > biggest_rate:
            biggest_rate = current_rate
            gbest_x = ap_loc.x
            gbest_y = ap_loc.y
        vel = ap_loc.vel_cal(w, c1, c2, gbest_x, gbest_y)
        ap_loc.move(vel[0], vel[1])
    if biggest_rate_l < biggest_rate:
        stale_count = 0
    else:
        stale_count += 1
    if stale_count >= max_stale_iterations:
        print(
            "Biggest rate has not changed for {} iterations. Exiting...".format(
                max_stale_iterations
            )
        )
        image_files = [
            "Week8/Output/{}Agent_{}.png".format(NUM_AP, i) for i in range(count)
        ]
        images = [imageio.imread(file) for file in image_files]
        imageio.mimsave("Week8\Demo\{}_agent.gif".format(NUM_AP), images, fps=7)
        break
    ax.text(
        10,
        10,
        "Best covered rate: " + str(biggest_rate) + "  " + str(count),
        fontsize=12,
    )
    fig.savefig("Week8/Output/{}Agent_{}.png".format(NUM_AP, count))

    # In ra tỷ lệ ô lưới được phủ sóng tốt nhất
    print("Best covered rate: " + str(biggest_rate) + "  " + str(count))
    biggest_rate_l = biggest_rate
    count += 1
