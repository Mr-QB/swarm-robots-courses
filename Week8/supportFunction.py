import random
from matplotlib.image import imread
import math
import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from Setting import *


# Hàm tính khoảng cách giữa hai điểm trong không gian 2D
def distanceCalculation(ob1_x, ob1_y, ob2_x, ob2_y):
    """
    Tính khoảng cách giữa hai điểm trong không gian 2D.

    Parameters:
        ob1_x (float): Tọa độ x của điểm thứ nhất.
        ob1_y (float): Tọa độ y của điểm thứ nhất.
        ob2_x (float): Tọa độ x của điểm thứ hai.
        ob2_y (float): Tọa độ y của điểm thứ hai.

    Returns:
        float: Khoảng cách giữa hai điểm.
    """
    distance_in_pixel = math.sqrt((ob2_x - ob1_x) ** 2 + (ob2_y - ob1_y) ** 2)
    distance_in_meter = distance_in_pixel * meter_pixel
    return distance_in_meter


# In ra vài dòng hướng dẫn
def printInstructions(screen):
    """
    In ra hướng dẫn trên màn hình.

    Parameters:
        screen (pygame.Surface): Màn hình Pygame.
    """
    font = pygame.font.Font(None, 17)
    text_1 = font.render('Press "S" to start the program', True, BLACK)
    text_2 = font.render('Press "ESC" to start the program', True, BLACK)
    screen.blit(text_1, (10, 10))
    screen.blit(text_2, (10, 25))


# def dBmToColor(dBm, min_dBm=-70, max_dBm=-30, cmap=cmap):
#     """
#     Chuyển đổi giá trị dBm thành màu sắc dựa trên colormap.

#     Parameters:
#         dBm (float): Giá trị dBm cần chuyển đổi.
#         min_dBm (float): Giá trị dBm tối thiểu trong phạm vi chuyển đổi, mặc định là -70.
#         max_dBm (float): Giá trị dBm tối đa trong phạm vi chuyển đổi, mặc định là -30.
#         cmap (LinearSegmentedColormap): Colormap được sử dụng, mặc định là cmap.

#     Returns:
#         tuple: Màu sắc tương ứng với giá trị dBm.
#     """
#     # Chuẩn hóa giá trị dBm vào khoảng [0, 1]
#     norm = (dBm - min_dBm) / (max_dBm - min_dBm)
#     norm = np.clip(norm, 0, 1)
#     return cmap(norm)


# Hàm chuyển đổi màu từ định dạng [0, 1] sang [0, 255]
def convertColor(color):
    """
    Chuyển đổi màu từ định dạng [0, 1] sang [0, 255].

    Parameters:
        color (tuple): Màu sắc ở định dạng [0, 1] cần chuyển đổi.

    Returns:
        tuple: Màu sắc ở định dạng [0, 255].
    """
    r, g, b, _ = color
    return (int(r * 255), int(g * 255), int(b * 255))


# Hàm vẽ ô lưới
def draw_grid(ax):
    for x in range(0, window_width, cell_size):
        for y in range(0, window_height, cell_size):
            ax.add_patch(
                plt.Rectangle(
                    (x, y), cell_size, cell_size, fill=False, color="black", alpha=0.2
                )
            )
    ax.set_xlim(0, window_width)
    ax.set_ylim(0, window_height)


# Hàm tính công suất tín hiệu dựa trên khoảng cách từ nguồn phát
def signalCalculation(distance):
    """
    Tính công suất tín hiệu dựa trên khoảng cách từ nguồn phát.

    Parameters:
        distance (float): Khoảng cách từ nguồn phát đến điểm cần đo.

    Returns:
        float: Công suất tín hiệu tại khoảng cách đã cho.
    """
    if distance == 0:
        distance = 0.1
    FSPL = (
        20 * math.log10(distance)
        + 20 * math.log10(2.4 * 10**9)
        + 20 * math.log10(4 * math.pi / (3 * 10**8))
    )
    P = 0 - FSPL
    return P


# Hàm tính toán tâm của các ô lưới
def calculate_cell_centers():
    # Khởi tạo một danh sách để lưu trữ các tâm của các ô lưới
    centers = []

    # Duyệt qua các cột của lưới
    for x in range(cell_size // 2, window_width, cell_size):
        # Duyệt qua các dòng của lưới
        for y in range(cell_size // 2, window_height, cell_size):
            # Tạo một tọa độ (x, y) đại diện cho tâm của ô lưới và thêm vào danh sách
            centers.append((x, y))

    # Trả về danh sách các tâm của các ô lưới
    return centers


# Hàm vẽ agent
def draw_agent(ax, agent):
    ax.plot(agent.x, agent.y, "o", color="black", markersize=8)


def dBm_to_color(dBm, min_dBm=-70, max_dBm=-30, alpha=0.01):
    colors = [
        (0.0, 0.0, 1.0, alpha),  # Màu blue với alpha (trong suốt) được chỉ định
        (0.0, 1.0, 0.0, alpha),  # Màu green với alpha (trong suốt) được chỉ định
        (1.0, 1.0, 0.0, alpha),  # Màu yellow với alpha (trong suốt) được chỉ định
        (1.0, 0.0, 0.0, alpha),  # Màu red với alpha (trong suốt) được chỉ định
    ]
    cmap = LinearSegmentedColormap.from_list("wifi_signal", colors, N=256)
    norm = (dBm - min_dBm) / (max_dBm - min_dBm)
    norm = np.clip(norm, 0, 1)
    return cmap(norm)
