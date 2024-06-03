from supportFunction import *  # Import các hàm hỗ trợ từ file supportFunction.py
from Agent import Agent  # Import lớp Agent từ file Agent.py

# Khởi tạo Pygame
pygame.init()

# Tạo cửa sổ Pygame
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("WiFi Signal Optimization")

last_rate = 0

# Tạo các AP
NUM_AP = 3
w = 0.9
c1 = 1
c2 = 1

ap = []
for i in range(NUM_AP):
    x_init = random.randint(0, window_width)
    y_init = random.randint(0, window_height)
    ap.append(Agent(x_init, y_init, 0, screen))  # Khởi tạo các AP với vị trí ngẫu nhiên

# Danh sách lưu tọa độ tâm các ô
cell_centers = []


# Hàm tính toán tọa độ tâm các ô
def calculate_cell_centers():
    """
    Tính toán và lưu trữ tọa độ tâm của các ô trên màn hình.

    Returns:
        int: Số lượng ô được chia ra.
    """
    count = 0
    for x in range(cell_size // 2, window_width, cell_size):
        for y in range(cell_size // 2, window_height, cell_size):
            count += 1
            cell_centers.append((x, y))
    return count


# Số lượng các ô được chia ra
num_cell = calculate_cell_centers()

# Tọa độ tốt nhất toàn cục
gbest_x = window_width / 2
gbest_y = window_height / 2
biggest_rate = 0
count = 0

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tính toán tín hiệu WiFi và vẽ các ô
    for ap_agent in ap:
        cell_uncovered_count = 0
        for center in cell_centers:
            clorest_ap = 9999
            for ap_loc in ap:
                distance_to_ap = distanceCalculation(
                    ap_loc.x, ap_loc.y, center[0], center[1]
                )
                if distance_to_ap <= clorest_ap:
                    clorest_ap = distance_to_ap
                signal = signalCalculation(clorest_ap)
            color = dBmToColor(signal)
            color_rbg = convertColor(color)
            if signal <= -60:
                cell_uncovered_count += 1
            top_left = (center[0] - cell_size // 2, center[1] - cell_size // 2)
            pygame.draw.rect(
                screen, color_rbg, (*top_left, cell_size, cell_size), cell_size
            )

        # Tính toán tỷ lệ phủ sóng và cập nhật vị trí tốt nhất cá nhân
        current_rate = (num_cell - cell_uncovered_count) / num_cell * 100
        if current_rate >= last_rate:
            ap_agent.pbest_rate = current_rate
            last_rate = current_rate
            ap_agent.pbest_x = ap_agent.x
            ap_agent.pbest_y = ap_agent.y
        if current_rate > biggest_rate:
            gbest_x = ap_agent.x
            gbest_y = ap_agent.y
            biggest_rate = current_rate

        # Tính toán và di chuyển AP dựa trên thuật toán PSO
        vel = ap_agent.vel_cal(w, c1, c2, gbest_x, gbest_y)
        ap_agent.move(vel[0], vel[1])

    count += 1
    print("Best covered rate: " + str(biggest_rate) + "  " + str(count))
    if biggest_rate > 95:
        break

    # Cập nhật màn hình
    pygame.display.flip()
