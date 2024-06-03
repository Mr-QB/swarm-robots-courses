import pygame
from Setting import *
from supportFunction import *


# Lớp Agent
class Agent:
    def __init__(self, x, y, avoid_obstacle_range, max_speed, status, screen):
        """
        Khởi tạo một đối tượng Agent.

        Parameters:
            x (float): Tọa độ x ban đầu của Agent.
            y (float): Tọa độ y ban đầu của Agent.
            avoid_obstacle_range (float): Phạm vi tránh va chạm của Agent.
            max_speed (float): Tốc độ tối đa của Agent.
            status (str): Trạng thái ban đầu của Agent.
            screen (pygame.Surface): Màn hình Pygame để vẽ Agent.

        Returns:
            None
        """
        self.x = x
        self.y = y
        self.avoid_range = avoid_obstacle_range
        self.vel_x = 0
        self.vel_y = 0
        self.max_speed = max_speed
        self.status = status
        self.target_x = 0
        self.target_y = 0
        self.color = YELLOW
        self.screen = screen
        self.radius = AGENT_RADIUS

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
            end_x = int(self.x + VIEW_RANGE * math.cos(math.radians(i)))
            end_y = int(self.y + VIEW_RANGE * math.sin(math.radians(i)))
            pygame.draw.circle(self.screen, RED, (end_x, end_y), 1)

    def draw(self):
        """
        Vẽ Agent lên màn hình Pygame.

        Parameters:
            None

        Returns:
            None
        """
        pygame.draw.circle(
            self.screen, self.color, (int(self.x), int(self.y)), self.radius
        )
        self.drawVisibleArea()

    def moveToGoal(self, goal_x, goal_y, move_to_goal_scale):
        """
        Tính toán vector hướng để di chuyển Agent đến mục tiêu.

        Parameters:
            goal_x (float): Tọa độ x của mục tiêu.
            goal_y (float): Tọa độ y của mục tiêu.
            move_to_goal_scale (float): Hệ số điều chỉnh di chuyển đến mục tiêu.

        Returns:
            tuple: Vector hướng di chuyển tới mục tiêu.
        """
        distance = calculateDistance(self.x, self.y, goal_x, goal_y)
        if distance >= self.avoid_range:
            scale = self.avoid_range / distance
        else:
            scale = 1
        goal_vector_x = (goal_x - self.x) * scale * move_to_goal_scale
        goal_vector_y = (goal_y - self.y) * scale * move_to_goal_scale
        return goal_vector_x, goal_vector_y

    def isGoal(self, goal_x, goal_y):
        """
        Kiểm tra xem Agent đã đạt đến mục tiêu chưa.

        Parameters:
            goal_x (float): Tọa độ x của mục tiêu.
            goal_y (float): Tọa độ y của mục tiêu.

        Returns:
            bool: True nếu Agent đã đạt đến mục tiêu, False nếu chưa.
        """
        if self.x == goal_x and self.y == goal_y:
            self.color = GREEN
            self.status = "occupied"
            return True
        else:
            return False

    def avoidObstacle(self, other_x, other_y, avoid_obstacle_scale):
        """
        Tính toán vector tránh va chạm của Agent với vật thể khác.

        Parameters:
            other_x (float): Tọa độ x của vật thể khác.
            other_y (float): Tọa độ y của vật thể khác.
            avoid_obstacle_scale (float): Hệ số điều chỉnh tránh va chạm.

        Returns:
            tuple: Vector tránh va chạm.
        """
        distance = calculateDistance(self.x, self.y, other_x, other_y)
        if distance <= self.avoid_range:
            avoid_vector_x = (
                self.x - other_x + random.random() * 2
            ) * avoid_obstacle_scale
            avoid_vector_y = (
                self.y - other_y + random.random() * 2
            ) * avoid_obstacle_scale
        else:
            avoid_vector_x = 0
            avoid_vector_y = 0
        return avoid_vector_x, avoid_vector_y

    def move(self, vel_x, vel_y):
        """
        Di chuyển Agent theo vector tốc độ.

        Parameters:
            vel_x (float): Vector tốc độ theo phương x.
            vel_y (float): Vector tốc độ theo phương y.

        Returns:
            None
        """
        speed = math.sqrt(vel_x**2 + vel_y**2)
        if speed > self.max_speed:
            scale = self.max_speed / speed
            vel_x *= scale
            vel_y *= scale
            self.vel_x = vel_x
            self.vel_y = vel_y
        self.x += vel_x
        self.y += vel_y
