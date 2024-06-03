import pygame
from tools import *
from random import uniform
from matrix import *
from math import pi, sin, cos

class Boid:
    def __init__(self, x, y):
        """
        Khởi tạo một boid với các thuộc tính về vị trí, vận tốc, gia tốc, và màu sắc.

        Args:
        - x, y: Tọa độ ban đầu.
        """
        self.position = Vector(x, y)
        vec_x = uniform(-1, 1)
        vec_y = uniform(-1, 1)
        self.velocity = Vector(vec_x, vec_y)
        self.velocity.normalize()
        # Đặt một độ lớn ngẫu nhiên cho vận tốc
        self.velocity = self.velocity * uniform(1.5, 4)
        self.acceleration = Vector()
        self.color = (255, 255, 255)
        self.temp = self.color
        self.secondaryColor = (70, 70, 70)
        self.max_speed = 5
        self.max_length = 1
        self.size = 2
        self.stroke = 5
        self.angle = 0
        self.hue = 0
        self.toggles = {"separation": True, "alignment": True, "cohesion": True}
        self.values = {"separation": 0.1, "alignment": 0.1, "cohesion": 0.1}
        self.radius = 40
    
    def limits(self, width , height):
        """
        Giữ boid trong giới hạn của màn hình.

        Args:
        - width: Chiều rộng màn hình.
        - height: Chiều cao màn hình.
        """
        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = width

        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height

    def behaviour(self, flock):
        """
        Thực hiện hành vi của boid bằng cách áp dụng các quy tắc như tách biệt, căn chỉnh và sự đồng lòng.

        Args:
        - flock: Danh sách các boid trong đàn.
        """
        self.acceleration.reset()

        if self.toggles["separation"] == True:
            avoid = self.separation(flock)
            avoid = avoid * self.values["separation"]
            self.acceleration.add(avoid)

        if self.toggles["cohesion"]== True:
            coh = self.cohesion(flock)
            coh = coh * self.values["cohesion"]
            self.acceleration.add(coh)

        if self.toggles["alignment"] == True:
            align = self.alignment(flock)
            align = align * self.values["alignment"]
            self.acceleration.add(align)

    def separation(self, flockMates):
        """
        Thực hiện hành vi tách biệt để tránh đám đông các boid xung quanh.

        Args:
        - flockMates: Danh sách các boid trong đàn.
        
        Returns:
        - steering: Vector biểu thị lực lái.
        """
        total = 0
        steering = Vector()

        for mate in flockMates:
            dist = getDistance(self.position, mate.position)
            if mate is not self and dist < self.radius:
                temp = SubVectors(self.position,mate.position)
                temp = temp/(dist ** 2)
                steering.add(temp)
                total += 1

        if total > 0:
            steering = steering / total
            steering.normalize()
            steering = steering * self.max_speed
            steering = steering - self.velocity
            steering.limit(self.max_length)

        return steering
    
    def alignment(self, flockMates):
        """
        Thực hiện hành vi căn chỉnh để căn chỉnh với vận tốc của các boid xung quanh.

        Args:
        - flockMates: Danh sách các boid trong đàn.
        
        Returns:
        - steering: Vector biểu thị lực lái.
        """
        total = 0
        steering = Vector()

        for mate in flockMates:
            dist = getDistance(self.position, mate.position)
            if mate is not self and dist < self.radius:
                vel = mate.velocity.Normalize()
                steering.add(vel)
                mate.color = hsv_to_rgb( self.hue ,1, 1)
                total += 1

        if total > 0:
            steering = steering / total
            steering.normalize()
            steering = steering * self.max_speed
            steering = steering - self.velocity.Normalize()
            steering.limit(self.max_length)
        return steering

    def cohesion(self, flockMates):
        """
        Thực hiện hành vi đồng lòng để di chuyển về phía trung tâm của các boid xung quanh.

        Args:
        - flockMates: Danh sách các boid trong đàn.
        
        Returns:
        - steering: Vector biểu thị lực lái.
        """
        total = 0
        steering = Vector()

        for mate in flockMates:
            dist = getDistance(self.position, mate.position)
            if mate is not self and dist < self.radius:
                steering.add(mate.position)
                total += 1

        if total > 0:
            steering = steering / total
            steering = steering - self.position
            steering.normalize()
            steering = steering * self.max_speed
            steering = steering - self.velocity
            steering.limit(self.max_length)

        return steering

    def update(self):
        """
        Cập nhật vị trí, vận tốc và góc của boid dựa trên gia tốc của nó.
        """
        self.position = self.position + self.velocity
        self.velocity = self.velocity + self.acceleration
        self.velocity.limit(self.max_speed)
        self.angle = self.velocity.heading() + pi/2

    def Draw(self, screen, distance, scale):
        """
        Vẽ boid lên màn hình.

        Args:
        - screen: Đối tượng màn hình Pygame.
        - distance: Khoảng cách đến màn hình.
        - scale: Hệ số tỷ lệ.
        """
        ps = []
        points = [None for _ in range(3)]

        points[0] = [[0],[-self.size],[0]]
        points[1] = [[self.size//2],[self.size//2],[0]]
        points[2] = [[-self.size//2],[self.size//2],[0]]

        for point in points:
            rotated = matrix_multiplication(rotationZ(self.angle) , point)
            z = 1/(distance - rotated[2][0])

            projection_matrix = [[z, 0, 0], [0, z, 0]]
            projected_2d = matrix_multiplication(projection_matrix, rotated)

            x = int(projected_2d[0][0] * scale) + self.position.x
            y = int(projected_2d[1][0] * scale) + self.position.y
            ps.append((x, y))

        pygame.draw.polygon(screen, self.secondaryColor, ps)
        pygame.draw.polygon(screen, self.color, ps, self.stroke)
