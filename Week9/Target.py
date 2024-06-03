import pygame
from Setting import *


class Target:
    def __init__(self, x, y, screen):
        """
        Khởi tạo một đối tượng Target.

        Parameters:
            x (float): Tọa độ x ban đầu của Target.
            y (float): Tọa độ y ban đầu của Target.
            screen (pygame.Surface): Màn hình Pygame để vẽ Target.

        Returns:
            None
        """
        self.x = x
        self.y = y
        self.status = "free"
        self.screen = screen

    def draw(self):
        """
        Vẽ Target lên màn hình Pygame.

        Parameters:
            None

        Returns:
            None
        """
        if self.status == "free":
            pygame.draw.circle(self.screen, BLACK, (int(self.x), int(self.y)), 3)
        elif self.status == "unfree":
            pygame.draw.circle(self.screen, BLUE, (int(self.x), int(self.y)), 3)
        # else:
        #     print(self.status)
