import pygame
import sys
import math
from SETTING import *

class Node:
    def __init__(self, x, y, screen, id):
        """
        Khởi tạo một đối tượng Node.

        Parameters:
            x (float): Tọa độ x của Node.
            y (float): Tọa độ y của Node.
            screen: Màn hình pygame.
            id (int): ID của Node.

        Returns:
            None
        """
        self.x = x
        self.y = y
        self.knows = []
        self.neighbors = []
        self.routing_table = {}  # Bảng định tuyến
        self.radius = node_radius
        self.connection_distance = connection_distance
        self.screen = screen
        self.node_id = id
        self.show_routing_table = False

    def update_routing_table(self):
        """
        Cập nhật bảng định tuyến dựa trên thông tin từ các Node láng giềng.
        """
        for neighbor in self.neighbors:
            if neighbor != self:
                for dest_node, data in neighbor.routing_table.items():
                    distance = self.calculate_distance_to(neighbor) + data['distance']
                    next_hop = neighbor.node_id  
                    if dest_node not in self.routing_table or distance < self.routing_table[dest_node]['distance']:
                        self.routing_table[dest_node] = {'next_hop': next_hop, 'distance': round(distance, 2)}

    def calculate_distance_to(self, node):
        """
        Tính khoảng cách tới một Node cụ thể.

        Parameters:
            node (Node): Node cần tính khoảng cách tới.

        Returns:
            float: Khoảng cách tới Node.
        """
        return math.sqrt((self.x - node.x) ** 2 + (self.y - node.y) ** 2)
    
    def draw_routing_table(self):
        """
        Vẽ bảng định tuyến lên màn hình.
        """
        font = pygame.font.Font(None, 20)
        y_offset = 50
        for dest_node, data in self.routing_table.items():
            text = font.render("To node {}: Next hop {}, Distance {}".format(dest_node, data['next_hop'], data['distance']), True, BLACK)
            self.screen.blit(text, (self.x + 50, self.y + y_offset))
            y_offset += 20

    def draw(self):
        """
        Vẽ Node lên màn hình.
        """
        if self.show_routing_table :
            self.draw_routing_table()
        self.draw_connections()
        pygame.draw.circle(self.screen, BLACK, (self.x, self.y), self.radius)  # Vẽ node
        for i in range(0, 360, 10): # Vẽ vòng tròn bao quanh node
            end_x = int(self.x + self.connection_distance  * math.cos(math.radians(i)))
            end_y = int(self.y + self.connection_distance  * math.sin(math.radians(i)))
            pygame.draw.circle(self.screen, RED, (end_x, end_y), 1)  
        font = pygame.font.Font(None, 20)
        text = font.render("Node " + str(self.node_id), True, BLACK)
        self.screen.blit(text, (self.x - 20, self.y + 20))
    
    def is_neighbor(self):
        """
        Kiểm tra xem Node có là láng giềng với các Node khác không.
        """
        self.neighbors = []
        self.routing_table = {} 
        for node in self.knows: # Kiểm tra xem khoảng cách có nhỏ hơn ngưỡng kết nối không
            distance = math.sqrt((self.x - node.x)**2 + (self.y - node.y)**2)
            if distance < self.connection_distance:
                self.neighbors.append(node)
                self.routing_table[node.node_id] = {'next_hop': node.node_id, 'distance': round(distance, 2)}

    def draw_connections(self):
        """
        Vẽ các kết nối giữa Node và Node láng giềng lên màn hình.
        """
        for neighbor in self.neighbors:
            pygame.draw.line(self.screen, GREEN, (self.x, self.y), (neighbor.x, neighbor.y), 1)

    def update_position(self, new_x, new_y):
        """
        Cập nhật vị trí của Node.

        Parameters:
            new_x (float): Tọa độ x mới.
            new_y (float): Tọa độ y mới.

        Returns:
            None
        """
        self.x = new_x
        self.y = new_y
