from matplotlib.image import imread
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from Setting import *

# Hàm vẽ ô lưới
def drawGrid(ax):
    """
    Vẽ lưới ô trên subplot đã cho.

    Parameters:
        ax (AxesSubplot): Đối tượng subplot để vẽ lưới ô lên.

    Returns:
        None
    """
    for x in range(0, window_width, cell_size):
        for y in range(0, window_height, cell_size):
            ax.add_patch(
                plt.Rectangle(
                    (x, y), cell_size, cell_size, fill=False, color="black", alpha=0.01
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
def calculateCellCenters():
    """
    Tính toán và trả về tọa độ trung tâm của các ô lưới.

    Returns:
        list: Danh sách tọa độ trung tâm của các ô lưới.
    """
    # Khởi tạo một danh sách để lưu trữ các tâm của các ô lưới
    centers = []

    # Duyệt qua các cột của lưới
    for x in range(cell_size // 2, window_width, cell_size):
        # Duyệt qua các dòng của lưới
        for y in range(cell_size // 2, window_height, cell_size):
            # Tạo một tọa độ (x, y) đại diện cho tâm của ô lưới và thêm vào danh sách
            centers.append((x, y))

    # Trả về danh sách các tọa độ tâm của các ô lưới
    return centers


# Hàm chuyển đổi giá trị dBm thành màu sắc tương ứng
def dBmToColor(dBm, min_dBm=-70, max_dBm=-30, alpha=0.04):
    """
    Chuyển đổi giá trị dBm thành màu sắc tương ứng.

    Parameters:
        dBm (float): Giá trị dBm cần chuyển đổi.
        min_dBm (float): Giá trị dBm tối thiểu trong phạm vi. Mặc định là -70.
        max_dBm (float): Giá trị dBm tối đa trong phạm vi. Mặc định là -30.
        alpha (float): Độ trong suốt của màu. Mặc định là 0.04.

    Returns:
        LinearSegmentedColormap: Màu sắc tương ứng với giá trị dBm.
    """
    colors = [
        (0.0, 0.0, 1.0,
         alpha),  # Màu blue với alpha (trong suốt) được chỉ định
        (0.0, 1.0, 0.0,
         alpha),  # Màu green với alpha (trong suốt) được chỉ định
        (1.0, 1.0, 0.0,
         alpha),  # Màu yellow với alpha (trong suốt) được chỉ định
        (1.0, 0.0, 0.0, alpha),  # Màu red với alpha (trong suốt) được chỉ định
    ]
    cmap = LinearSegmentedColormap.from_list("wifi_signal", colors, N=256)
    norm = (dBm - min_dBm) / (max_dBm - min_dBm)
    norm = np.clip(norm, 0, 1)
    return cmap(norm)
