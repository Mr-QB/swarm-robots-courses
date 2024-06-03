import pygame
from Agent import *
from Target import *


# Khởi tạo Pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi-target Tracking")

targets_init = []
numbers_x = [random.choice(range(100, WIDTH - 100, 10)) for _ in range(NUM_AGENTS)]
numbers_y = [random.choice(range(100, HEIGHT - 150, 10)) for _ in range(NUM_AGENTS)]
for i in range(NUM_AGENTS):
    targets_init.append(Target(numbers_x[i], numbers_y[i], screen))


agents = []
for i in range(NUM_AGENTS):
    agents.append(
        Agent(
            random.randint(int(WIDTH / 2 - 150), int(WIDTH / 2 + 150)),
            random.randint(HEIGHT - 100, HEIGHT - 10),
            AVOID_RANGE,
            MAX_SPEED,
            "unassigned",
            screen,
        )
    )


# Hàm chính
def main():
    # Vẽ bản đồ
    running = True
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
        for tar in targets_init:
            tar.draw()
            # tìm kiếm đích:
        # Duyệt qua mỗi agent để tìm các targets có thể tiếp cận.
        for agent_find in agents:
            # Duyệt qua mỗi target để kiểm tra trạng thái và khoảng cách tới agent.
            for target_agent in targets_init:
                if (
                    target_agent.status == "free"
                ):  # Nếu target chưa được gán cho agent nào.
                    # Tính khoảng cách từ agent đến target.
                    distance_to_target_agent = calculateDistance(
                        agent_find.x, agent_find.y, target_agent.x, target_agent.y
                    )
                    # Nếu khoảng cách nhỏ hơn hoặc bằng VIEW_RANGE (phạm vi nhìn thấy).
                    if distance_to_target_agent <= VIEW_RANGE:
                        target_agent.status = (
                            "finded"  # Đánh dấu target đã được tìm thấy.
                        )

        # phân công các agent:
        # Duyệt qua mỗi target để phân công agent cho target đã tìm thấy.
        for target_assignment in targets_init:
            if target_assignment.status == "finded":  # Nếu target đã được tìm thấy.
                closest_distance = float("inf")  # Khởi tạo khoảng cách lớn nhất.
                for agent_assignment in agents:
                    if (
                        agent_assignment.status == "unassigned"
                    ):  # Nếu agent chưa được phân công.
                        # Tính khoảng cách từ agent đến target.
                        distance_to_target_agent = calculateDistance(
                            agent_assignment.x,
                            agent_assignment.y,
                            target_assignment.x,
                            target_assignment.y,
                        )
                        # Nếu khoảng cách nhỏ hơn hoặc bằng closest_distance.
                        if distance_to_target_agent <= closest_distance:
                            closest_agent = agent_assignment  # Gán agent gần nhất.
                            closest_distance = distance_to_target_agent
                closest_agent.status = "assigned"  # Đánh dấu agent đã được phân công.
                closest_agent.target_x = (
                    target_assignment.x
                )  # Gán tọa độ x của target cho agent.
                closest_agent.target_y = (
                    target_assignment.y
                )  # Gán tọa độ y của target cho agent.
                target_assignment.status = (
                    "unfree"  # Đánh dấu target đã được phân công.
                )

        # di chuyển các agent dựa vào trạng thái:
        for agent in agents:
            if agent.status == "occupied":  # Nếu agent đang bận.
                pass
            elif agent.status == "assigned":  # Nếu agent đã được phân công.
                agent.color = RED  # Thay đổi màu của agent thành màu đỏ.
                # Tính vector di chuyển tới mục tiêu dựa trên mục tiêu và hệ số di chuyển.
                goal_vector_x, goal_vector_y = agent.moveToGoal(
                    agent.target_x, agent.target_y, MOVE_TO_GOAL_SCALE
                )
                move_vector_x, move_vector_y = goal_vector_x, goal_vector_y
                for other_agent in agents:
                    if (
                        other_agent != agent
                    ):  # Nếu agent khác không phải agent hiện tại.
                        # Tính vector tránh va chạm dựa trên agent khác và hệ số tránh va chạm.
                        avoid_vector_x, avoid_vector_y = agent.avoidObstacle(
                            other_agent.x, other_agent.y, AVOIDANCE_SCALE
                        )
                        move_vector_x += avoid_vector_x  # Cộng thêm vector tránh va chạm vào vector di chuyển.
                        move_vector_y += avoid_vector_y
                agent.move(move_vector_x, move_vector_y)  # Di chuyển agent.
            elif agent.status == "unassigned":  # Nếu agent chưa được phân công.
                # Tính toán hướng di chuyển dựa trên các đối tượng đã được phân công.
                move_vector_x, move_vector_y = 0.15, 0.25
                for assigned_agent in agents:
                    if assigned_agent.status == "assigned":
                        # Tính vector di chuyển từ agent chưa phân công đến agent đã phân công.
                        distance_to_assigned_agent = calculateDistance(
                            agent.x, agent.y, assigned_agent.x, assigned_agent.y
                        )
                        # Tính toán hướng di chuyển để cách xa khi gần và lại gần khi xa.
                        avoidance_factor = 1 / (
                            distance_to_assigned_agent**1.46
                        )  # Hệ số tránh va chạm
                        move_vector_x += (assigned_agent.x - agent.x) * avoidance_factor
                        move_vector_y += (assigned_agent.y - agent.y) * avoidance_factor
                # Di chuyển agent theo hướng tính được.
                agent.move(move_vector_x, move_vector_y)

            agent.isGoal(
                agent.target_x, agent.target_y
            )  # Kiểm tra xem agent đã đạt đến mục tiêu chưa.
            agent.draw()  # Vẽ agent lên màn hình.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        pygame.time.Clock().tick(30)


if __name__ == "__main__":
    main()
