import pygame
import math
import random
from supportFunction import *


class Agent:
    def __init__(self, x, y, avoid_obstacle_range, max_speed, radius, screen):
        """
        Khởi tạo một đối tượng Agent.

        Parameters:
            x (float): Tọa độ x của Agent.
            y (float): Tọa độ y của Agent.
            avoid_obstacle_range (float): Khoảng cách tránh vật cản.
            max_speed (float): Tốc độ tối đa của Agent.
            radius (float): Bán kính tạo ra các điểm mục tiêu xung quanh.
            screen: Màn hình pygame.

        Returns:
            None
        """
        self.x = x
        self.y = y
        self.avoid_range = avoid_obstacle_range
        self.max_speed = max_speed
        self.gen_radius = radius
        self.screen = screen

    def draw(self, color):
        """
        Vẽ Agent trên màn hình.

        Parameters:
            color: Màu sắc của Agent.

        Returns:
            None
        """
        pygame.draw.circle(self.screen, color, (int(self.x), int(self.y)), 8)

    def drawVisibleArea(self):
        """
        Vẽ vùng quan sát của node.

        Hàm này vẽ một vòng tròn xung quanh node để thể hiện vùng quan sát của node.

        Parameters:
            None

        Returns:
            None
        """
        for i in range(0, 360, 10):  # Vẽ vòng tròn bao quanh node
            end_x = int(self.x + self.gen_radius * math.cos(math.radians(i)))
            end_y = int(self.y + self.gen_radius * math.sin(math.radians(i)))
            pygame.draw.circle(self.screen, RED, (end_x, end_y), 1)

    def moveToGoal(self, goal_x, goal_y):
        """
        Di chuyển Agent đến mục tiêu.

        Parameters:
            goal_x (float): Tọa độ x của mục tiêu.
            goal_y (float): Tọa độ y của mục tiêu.

        Returns:
            list: Vector hướng di chuyển tới mục tiêu.
        """
        distance = calculateDistance(self.x, self.y, goal_x, goal_y)
        if distance >= self.avoid_range:
            scale = self.avoid_range / distance
        else:
            scale = 1
        goal_vector_x = (goal_x - self.x) * scale
        goal_vector_y = (goal_y - self.y) * scale
        goal_vector = [goal_vector_x, goal_vector_y]
        return goal_vector

    def avoidObstacle(self, other_x, other_y, avoid_obstacle_scale):
        """
        Tránh các vật cản.

        Parameters:
            other_x (float): Tọa độ x của vật cản.
            other_y (float): Tọa độ y của vật cản.
            avoid_obstacle_scale (float): Hệ số tránh vật cản.

        Returns:
            list: Vector tránh vật cản.
        """
        distance = calculateDistance(self.x, self.y, other_x, other_y)
        if distance <= self.avoid_range:
            avoid_vector_x = (
                self.x - other_x + random.random() * 1
            ) * avoid_obstacle_scale
            avoid_vector_y = (
                self.y - other_y + random.random() * 1
            ) * avoid_obstacle_scale
        else:
            avoid_vector_x = 0
            avoid_vector_y = 0
        avoid_vector = [avoid_vector_x, avoid_vector_y]
        return avoid_vector

    def isGoal(self, goal_x, goal_y):
        """
        Kiểm tra xem Agent đã đạt được mục tiêu chưa.

        Parameters:
            goal_x (float): Tọa độ x của mục tiêu.
            goal_y (float): Tọa độ y của mục tiêu.

        Returns:
            bool: True nếu Agent đạt được mục tiêu, False nếu không.
        """
        if self.x == goal_x and self.y == goal_y:
            return True
        else:
            return False

    def move(self, vel_x, vel_y):
        """
        Di chuyển Agent theo vector tốc độ.

        Parameters:
            vel_x (float): Thay đổi tọa độ x theo vector tốc độ.
            vel_y (float): Thay đổi tọa độ y theo vector tốc độ.

        Returns:
            None
        """
        speed = math.sqrt(vel_x**2 + vel_y**2)
        if speed > self.max_speed:
            scale = self.max_speed / speed
            vel_x *= scale
            vel_y *= scale
        self.x += vel_x
        self.y += vel_y
