import pygame
import sys
import random
import math
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Khởi tạo Pygame
pygame.init()
# Kích thước cửa sổ
window_width = 800
window_height = 600

# Kích thước ô
cell_size = 10
# Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
# hệ số meter / pixel
# 1 pixel = 30cm
meter_pixel = 3 / 100


def distanceCalculation(ob1_x, ob1_y, ob2_x, ob2_y):
    distance_in_pixel = math.sqrt((ob2_x - ob1_x) ** 2 + (ob2_y - ob1_y) ** 2)
    distance_in_meter = distance_in_pixel * meter_pixel
    return distance_in_meter


def signalCalculation(distance):
    if distance == 0:
        distance = 0.1
    FSPL = (
        20 * math.log10(distance)
        + 20 * math.log10(2.4 * 10**9)
        + 20 * math.log10(4 * math.pi / (3 * 10**8))
    )
    P = 0 - FSPL
    return P


# Định nghĩa dải màu gradient
colors = ["blue", "green", "yellow", "red"]
alpha_values = [1.0, 1.0, 1.0, 0.0]
cmap = LinearSegmentedColormap.from_list(
    "wifi_signal", list(zip(colors, alpha_values)), N=256
)


# Hàm chuyển đổi giá trị dBm thành màu sắc
def dBm_to_color(dBm, min_dBm=-70, max_dBm=-30, cmap=cmap):
    # Chuẩn hóa giá trị dBm vào khoảng [0, 1]
    norm = (dBm - min_dBm) / (max_dBm - min_dBm)
    norm = np.clip(norm, 0, 1)
    return cmap(norm)


def convert_color(color):
    """Chuyển đổi màu từ định dạng [0, 1] sang [0, 255]"""
    r, g, b, _ = color
    return (int(r * 255), int(g * 255), int(b * 255))


# agent
class Agent:
    def __init__(self, x, y, pbest_rate):
        self.x = x
        self.y = y
        self.vel_x = random.random() * 10
        self.vel_y = random.random() * 10
        self.pbest_x = x
        self.pbest_y = x
        self.pbest_rate = pbest_rate

    def draw(self, color):
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 8)

    def vel_cal(self, w, c1, c2, gbest_x, gbest_y):
        vel_x = (
            w * self.vel_x
            + c1 * random.random() * (self.pbest_x - self.x)
            + c2 * random.random() * (gbest_x - self.x)
        )
        self.vel_x = vel_x
        vel_y = (
            w * self.vel_y
            + c1 * random.random() * (self.pbest_y - self.y)
            + c2 * random.random() * (gbest_y - self.y)
        )
        self.vel_y = vel_y
        vel_vector = [vel_x, vel_y]
        return vel_vector

    def move(self, vel_x, vel_y):
        self.x += vel_x
        self.y += vel_y


# Tạo cửa sổ
screen = pygame.display.set_mode((window_width, window_height))
background_image = pygame.image.load(
    "D:\Dev\Multi-RobotCourses\Week8\Input\house_cad.png"
).convert()
pygame.display.set_caption("Window")

last_rate = 0

# Tạo các agent
NUM_AP = 3
w = 0.9
c1 = 1
c2 = 1

ap = []
for i in range(NUM_AP):
    x_init = random.randint(0, window_width)
    y_init = random.randint(0, window_height)
    ap.append(Agent(x_init, y_init, 0))


# Danh sách lưu tọa độ tâm các ô
cell_centers = []


# Hàm tính toán tọa độ tâm các ô
def calculate_cell_centers():
    count = 0
    for x in range(cell_size // 2, window_width, cell_size):
        for y in range(cell_size // 2, window_height, cell_size):
            count += 1
            cell_centers.append((x, y))
    return count


# Số lượng các cell được chia ra


# Tính toán tọa độ tâm các ô
num_cell = calculate_cell_centers()
gbest_x = window_width / 2
gbest_y = window_height / 2
biggest_rate = 0
count = 0
# Vòng lặp chính
while True:
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for ap_agent in ap:
        # Xác định RSSI ở từng ô
        cell_uncovered_count = 0
        for center in cell_centers:
            clorest_ap = 9999
            for ap_loc in ap:
                ditance_to_ap = distanceCalculation(
                    ap_loc.x, ap_loc.y, center[0], center[1]
                )

                if ditance_to_ap <= clorest_ap:
                    clorest_ap = ditance_to_ap
                signal = signalCalculation(clorest_ap)
            color = dBm_to_color(signal)
            color_rbg = convert_color(color)
            if signal <= -60:
                cell_uncovered_count += 1
            # Tính toán tọa độ của các góc của ô để vẽ
            top_left = (center[0] - cell_size // 2, center[1] - cell_size // 2)
            pygame.draw.rect(
                screen, color_rbg, (*top_left, cell_size, cell_size), cell_size
            )
        current_rate = (num_cell - cell_uncovered_count) / num_cell * 100
        # print(current_rate)
        if current_rate >= last_rate:
            ap_agent.pbest_rate = current_rate
            last_rate = current_rate
            ap_agent.pbest_x = ap_agent.x
            ap_agent.pbest_y = ap_agent.y
        if current_rate > biggest_rate:
            gbest_x = ap_agent.x
            gbest_y = ap_agent.y
            biggest_rate = current_rate
        vel = ap_agent.vel_cal(w, c1, c2, gbest_x, gbest_y)
        ap_agent.move(vel[0], vel[1])

        # for ap_draw in ap:
        #     ap_draw.draw(white)
    count += 1
    print("Best covered rate: " + str(biggest_rate) + "  " + str(count))
    if biggest_rate > 95:
        break
    # Cập nhật màn hình
    pygame.display.flip()
