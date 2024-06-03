import random
import math
import numpy as np
from Setting import *
import pygame


def calculateDistance(x1, y1, x2, y2):
    """
    Tính toán khoảng cách giữa hai điểm trong không gian 2D.

    Parameters:
        x1 (float): Tọa độ x của điểm 1.
        y1 (float): Tọa độ y của điểm 1.
        x2 (float): Tọa độ x của điểm 2.
        y2 (float): Tọa độ y của điểm 2.

    Returns:
        float: Khoảng cách giữa hai điểm.
    """
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance


def addArrays(array1, array2):
    """
    Thực hiện phép cộng các phần tử tương ứng của hai mảng.

    Parameters:
        array1 (list): Mảng 1.
        array2 (list): Mảng 2.

    Returns:
        list: Mảng kết quả sau khi thực hiện phép cộng.
    """
    result = []
    for i in range(len(array1)):
        result.append(array1[i] + array2[i])
    return result


def findMatchingColumn2d(array_2d, new_column):
    """
    Tìm kiếm một cột trong mảng 2D có giá trị giống với một cột mới cho trước.

    Parameters:
        array_2d (numpy.array): Mảng 2D.
        new_column (numpy.array): Cột mới cần tìm kiếm.

    Returns:
        bool: True nếu tìm thấy cột giống nhau, False nếu không.
    """
    for i in range(array_2d.shape[1]):
        if array_2d[0][i] == new_column[0][0] and array_2d[1][i] == new_column[1][0]:
            return True
    return False


def drawMap(numberObstacles=8):
    """
    Vẽ bản đồ với các chướng ngại vật được tạo ngẫu nhiên.

    Parameters:
        numberObstacles (int): Số lượng chướng ngại vật. Mặc định là 8.

    Returns:
        list: Danh sách các hình chữ nhật biểu diễn các chướng ngại vật.
        list: Danh sách các tường biên của các chướng ngại vật.
        numpy.array: Mảng 2D biểu diễn khu vực tránh.
                     Mỗi cột của mảng này biểu diễn một điểm trên bản đồ mà robot nên tránh.
    """
    square_rect = []
    num_rectangles = numberObstacles
    for _ in range(num_rectangles):
        x = np.random.randint(0, WIDTH - 150)
        y = np.random.randint(0, HEIGHT - 150)
        width = np.random.randint(50, 150)
        height = np.random.randint(50, 150)
        square_rect.append([x, y, width, height])

    walls = []
    for i in range(numberObstacles):
        for j in range(square_rect[i][0], square_rect[i][0] + square_rect[i][2], 5):
            for k in range(square_rect[i][1], square_rect[i][1] + square_rect[i][3], 5):
                walls.append((j, k))

    target_avoid_area = np.array([[9999], [9999]])
    for i in range(numberObstacles):
        for j in range(
            square_rect[i][0] - 10, square_rect[i][0] + square_rect[i][2] + 10
        ):
            for k in range(
                square_rect[i][1] - 10, square_rect[i][1] + square_rect[i][3] + 10
            ):
                new_column = np.array([[j], [k]])
                target_avoid_area = np.concatenate(
                    (target_avoid_area, new_column), axis=1
                )

    return square_rect, walls, target_avoid_area


# In ra vài dòng hướng dẫn
def printInstructions(screen):
    font = pygame.font.Font(None, 17)
    text_1 = font.render('Press "S" to start the program', True, BLACK)
    text_2 = font.render('Press "ESC" to start the program', True, BLACK)
    screen.blit(text_1, (10, 10))
    screen.blit(text_2, (10, 25))
