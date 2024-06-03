import pygame
import sys
import random
from SETTING import *
from Node import Node

# Khởi tạo Pygame
pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("DSDV Demo")

clock = pygame.time.Clock()

nodes = []  # tập hợp các node


def createNewNode():  # Tạo node mới
    nodes.append(
        Node(
            random.randint(0, WINDOW_SIZE[0]),
            random.randint(0, WINDOW_SIZE[1]),
            screen,
            len(nodes),
        )
    )
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if j != i:
                nodes[i].knows.append(nodes[j])


# In ra vài dòng hướng dẫn
def printInstructions():
    font = pygame.font.Font(None, 17)
    text_1 = font.render('Press "N" to add a new node', True, BLACK)
    text_2 = font.render("Use the mouse to move Nodes", True, BLACK)
    screen.blit(text_1, (10, 10))
    screen.blit(text_2, (10, 25))


# Vòng lặp chính
running = True
dragging = False
selected_node = None
selected_node_show_routing_table = None
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                createNewNode()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for node in nodes:
                    distance = (
                        (node.x - event.pos[0]) ** 2 + (node.y - event.pos[1]) ** 2
                    ) ** 0.5
                    if distance <= node.radius:
                        dragging = True
                        selected_node = node
                        selected_node.show_routing_table = True
                    else:
                        node.show_routing_table = False
                    node.is_neighbor()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                selected_node = None
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                selected_node.update_position(event.pos[0], event.pos[1])
                node.is_neighbor()

    for node in nodes:
        node.draw()
        node.update_routing_table()

    printInstructions()
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()
