import pygame
import sys
import math
import numpy as np

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Số lượng agent
NUM_AGENTS = 9
AGENT_SPACE = 15
WING_ANGLE = math.pi / 1.5
MAX_SPEED = 0.1

# Tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("V-Shape Formation")


def rotate_vector(x, y, alpha):
    """
    Xoay một vector (x, y) theo góc alpha.

    Args:
    - x, y: Tọa độ của vector.
    - alpha: Góc xoay (rad).

    Returns:
    - rotated_x, rotated_y: Tọa độ của vector sau khi được xoay.
    """
    # Tạo ma trận xoay
    rotation_matrix = np.array(
        [[math.cos(alpha), -math.sin(alpha)], [math.sin(alpha), math.cos(alpha)]]
    )

    # Tạo vector cột từ (x, y)
    vector = np.array([[x], [y]])

    # Thực hiện phép nhân ma trận để xoay vector
    rotated_vector = np.dot(rotation_matrix, vector)

    # Trích xuất thành phần x và y của vector sau khi được xoay
    rotated_x, rotated_y = rotated_vector[0][0], rotated_vector[1][0]

    return rotated_x, rotated_y


def limit_speed(vel_x, vel_y, max_speed):
    """
    Giới hạn tốc độ của một vector vận tốc.

    Args:
    - vel_x, vel_y: Thành phần x và y của vector vận tốc.
    - max_speed: Giới hạn tốc độ.

    Returns:
    - vel_x, vel_y: Thành phần x và y của vector vận tốc sau khi được giới hạn.
    """
    speed = math.sqrt(vel_x**2 + vel_y**2)
    if speed > max_speed:
        scale = max_speed / speed
        vel_x *= scale
        vel_y *= scale
    return vel_x, vel_y


# Lớp Agent
class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, color, goal_x, goal_y):
        """
        Vẽ một agent trên màn hình với hướng đỉnh luôn hướng về mục tiêu.

        Args:
        - color: Màu sắc của agent.
        - goal_x: Tọa độ x của mục tiêu.
        - goal_y: Tọa độ y của mục tiêu.
        """
        # Tính toán góc giữa vị trí hiện tại của agent và mục tiêu
        angle_to_goal = math.atan2(goal_y - self.y, goal_x - self.x)
        
        # Tạo điểm cho các đỉnh của tam giác (xoay tam giác theo góc tính được)
        rotated_points = [
            (int(self.x + 12 * math.cos(angle_to_goal)), int(self.y + 12 * math.sin(angle_to_goal))),
            (int(self.x + 6 * math.cos(angle_to_goal - math.pi / 6)), int(self.y + 6 * math.sin(angle_to_goal - math.pi / 6))),
            (int(self.x + 6 * math.cos(angle_to_goal + math.pi / 6)), int(self.y + 6 * math.sin(angle_to_goal + math.pi / 6)))
        ]
        
        # Vẽ tam giác
        pygame.draw.polygon(screen, color, rotated_points)
    def center_agent_move(self, goal_x, goal_y):
        """
        Di chuyển agent ở vị trí trung tâm.

        Args:
        - goal_x, goal_y: Tọa độ mục tiêu.
        """
        dx = goal_x - self.x
        dy = goal_y - self.y
        vel_x, vel_y = limit_speed(dx, dy, MAX_SPEED / 2)
        self.x += vel_x
        self.y += vel_y

    def left_wing_agent_move(self, goal_x, goal_y, center_x, center_y, center_distance):
        """
        Di chuyển agent ở cánh trái.

        Args:
        - goal_x, goal_y: Tọa độ mục tiêu.
        - center_x, center_y: Tọa độ của agent ở vị trí trung tâm.
        - center_distance: Khoảng cách từ agent cánh trái đến agent ở vị trí trung tâm.
        """
        alpha = math.atan2(goal_y - center_y, goal_x - center_x)
        rotated_x, rotated_y = rotate_vector(
            -center_distance * AGENT_SPACE * math.cos(WING_ANGLE / 2),
            center_distance * AGENT_SPACE * math.sin(WING_ANGLE / 2),
            alpha,
        )
        dx = rotated_x + center_x - self.x
        dy = rotated_y + center_y - self.y
        vel_x, vel_y = limit_speed(dx, dy, MAX_SPEED)
        self.x += vel_x
        self.y += vel_y

    def right_wing_agent_move(
        self, goal_x, goal_y, center_x, center_y, center_distance
    ):
        """
        Di chuyển agent ở cánh phải.

        Args:
        - goal_x, goal_y: Tọa độ mục tiêu.
        - center_x, center_y: Tọa độ của agent ở vị trí trung tâm.
        - center_distance: Khoảng cách từ agent cánh phải đến agent ở vị trí trung tâm.
        """
        alpha = math.atan2(goal_y - center_y, goal_x - center_x)
        rotated_x, rotated_y = rotate_vector(
            -center_distance * AGENT_SPACE * math.cos(WING_ANGLE / 2),
            -center_distance * AGENT_SPACE * math.sin(WING_ANGLE / 2),
            alpha,
        )
        dx = rotated_x + center_x - self.x
        dy = rotated_y + center_y - self.y
        vel_x, vel_y = limit_speed(dx, dy, MAX_SPEED)
        self.x += vel_x
        self.y += vel_y


# Tạo danh sách agent
agents = []
for i in range(NUM_AGENTS):
    agents.append(Agent(WIDTH // 2, HEIGHT // 2))


# Hàm chính
def main():
    running = True
    while running:
        screen.fill(BLACK)
        # Lấy tọa độ của chuột
        goal_x, goal_y = pygame.mouse.get_pos()
        if NUM_AGENTS % 2 == 0:
            center_pos = NUM_AGENTS / 2 - 1
        else:
            center_pos = NUM_AGENTS / 2
        center_pos = int(center_pos)
        # Di chuyển các agent theo con trỏ chuột
        agents[center_pos].center_agent_move(goal_x, goal_y)
        agents[center_pos].draw(RED,goal_x, goal_y)
        center_x = agents[center_pos].x
        center_y = agents[center_pos].y
        for i in range(0, center_pos):
            agents[i].right_wing_agent_move(
                goal_x, goal_y, center_x, center_y, center_pos - i
            )
            agents[i].draw(WHITE,goal_x, goal_y)
        for i in range(center_pos +1, NUM_AGENTS):
            agents[i].left_wing_agent_move(
                goal_x, goal_y, center_x, center_y, i - center_pos
            )
            agents[i].draw(WHITE,goal_x, goal_y)
        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
