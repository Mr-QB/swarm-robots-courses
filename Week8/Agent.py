from supportFunction import *


# Lớp Agent đại diện cho các AP
# Lớp Agent đại diện cho các AP
class Agent:

    def __init__(self, x, y, pbest_rate):
        """
        Khởi tạo một đối tượng Agent.

        Parameters:
            x (float): Tọa độ x ban đầu của Agent.
            y (float): Tọa độ y ban đầu của Agent.
            pbest_rate (float): Tỷ lệ covered rate tốt nhất của Agent.
        """
        self.x = x
        self.y = y
        self.vel_x = random.random() * 10
        self.vel_y = random.random() * 10
        self.pbest_x = x
        self.pbest_y = x
        self.pbest_rate = pbest_rate

    # # Vẽ AP trên màn hình
    # def draw(self, color):
    #     """
    #     Vẽ Agent (AP) trên màn hình.

    #     Parameters:
    #         color (tuple): Màu sắc của Agent.
    #     """
    #     pygame.draw.circle(self.screen, color, (int(self.x), int(self.y)), 8)

    # Tính toán vận tốc của AP dựa trên thuật toán PSO
    def vel_cal(self, w, c1, c2, gbest_x, gbest_y):
        """
        Tính toán vector vận tốc của Agent dựa trên thuật toán PSO.

        Parameters:
            w (float): Hệ số trọng số quán tính.
            c1 (float): Hệ số học tập cá nhân.
            c2 (float): Hệ số học tập cộng đồng.
            gbest_x (float): Tọa độ x của global best.
            gbest_y (float): Tọa độ y của global best.

        Returns:
            list: Vector vận tốc mới.
        """
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

    # Di chuyển AP
    def move(self, vel_x, vel_y):
        """
        Di chuyển Agent (AP) dựa trên vector vận tốc.

        Parameters:
            vel_x (float): Giá trị vận tốc theo trục x.
            vel_y (float): Giá trị vận tốc theo trục y.
        """
        self.x += vel_x
        self.y += vel_y
