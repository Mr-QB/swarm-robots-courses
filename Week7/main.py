import pygame
import sys
import math
from supportFunction import *
from Agent import Agent

# Khởi tạo Pygame
pygame.init()


# Tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coverage Swarm Controll")


# Tạo danh sách agent
agents = []
for i in range(NUM_AGENTS):
    agents.append(Agent(-10, 150, AVOID_RANGE, MAX_SPEED, GEN_RADIUS,screen=screen))

# Hàm chính
def main():
    # Khởi tạo màn hình pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Swarm Control")

    # Tạo bản đồ với số lượng chướng ngại vật và kích thước mặc định
    square_rect, walls, target_avoid_area = drawMap(NUMBEROBSTACLES)

    # Khởi tạo biến và vị trí ban đầu cho robot
    running = True
    target = np.array([[120], [150]])
    occupied_target = np.array([[9999], [9999]])
    start = 0
    start_simulation = False
    while not start_simulation:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    start_simulation = True
        screen.fill(WHITE)
        printInstructions(screen)
        pygame.display.flip()
    while running:
        screen.fill(WHITE)
        printInstructions(screen)
        # Lấy vị trí mục tiêu mới
        goal_x = target[0][0]
        goal_y = target[1][0]
        goal_column = np.array([[goal_x],[goal_y]])

        # Kiểm tra xem vị trí mục tiêu có bị chiếm dụng hay không
        if findMatchingColumn2d(occupied_target, goal_column):
            target = np.delete(target, 0, axis=1)
        else:
            # Di chuyển robot đến vị trí mục tiêu và xử lý các tương tác với chướng ngại vật
            agent = agents[start]
            obstacle_vector = [0, 0]
            goal_vector = agent.moveToGoal(goal_x, goal_y)
            for other_agent in agents:
                if other_agent != agent:
                    avoid_vector = agent.avoidObstacle(other_agent.x, other_agent.y, AVOID_OBSTACLE_SCALE)
                    obstacle_vector = addArrays(obstacle_vector, avoid_vector)
            for wall in walls:
                avoid_vector = agent.avoidObstacle(wall[0], wall[1], AVOID_OBSTACLE_SCALE)
                obstacle_vector = addArrays(obstacle_vector, avoid_vector)
            
            velocity = [0, 0]
            velocity = addArrays(velocity, goal_vector)
            velocity = addArrays(velocity, obstacle_vector)
            agent.move(velocity[0], velocity[1])

            # Nếu robot đạt được mục tiêu, tạo các mục tiêu mới xung quanh vị trí hiện tại
            if agent.isGoal(goal_x, goal_y):
                occupied_target = np.concatenate((occupied_target, [[goal_x], [goal_y]]), axis=1)
                for i in range(6):
                    angle = i * math.pi / 3
                    new_target_x = agent.x + agent.gen_radius * math.cos(angle)
                    new_target_x = round(new_target_x)
                    new_target_y = agent.y + agent.gen_radius * math.sin(angle)
                    new_target_y = round(new_target_y)
                    if 0 < new_target_x < WIDTH and 0 < new_target_y < HEIGHT:
                        new_column = np.array([[new_target_x], [new_target_y]])
                        if not findMatchingColumn2d(target_avoid_area, new_column):
                            target = np.concatenate((target, new_column), axis=1)
                start += 1
                target = np.delete(target, 0, axis=1)

            # Vẽ các điểm mục tiêu mới và các robot trên màn hình
            num_col = target.shape[1]
            for i in range(num_col):
                pygame.draw.circle(screen, GREEN, (target[0][i], target[1][i]), 5)
            for agent_draw in agents:
                if agent_draw == agent:
                    agent_draw.draw(RED)
                else:
                    agent_draw.draw(BLUE)
                    agent_draw.drawVisibleArea()
            pygame.draw.circle(screen, YELLOW, (goal_x, goal_y), 5)

        # Vẽ các chướng ngại vật lên màn hình
        for i in range(8):
            square_rect_draw = pygame.Rect(square_rect[i][0], square_rect[i][1], square_rect[i][2], square_rect[i][3])
            pygame.draw.rect(screen, BLACK, square_rect_draw)
        
        # Xử lý sự kiện thoát
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Cập nhật màn hình
        pygame.display.flip()

    # Kết thúc chương trình
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

