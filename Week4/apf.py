import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
import matplotlib
import matplotlib.cm as cm

matplotlib.use("TkAgg")

# Define constants and variables
show_animation = True  # Xác định liệu bạn muốn hiển thị hoạt hình trong quá trình di chuyển của robot hay không
SIM_TIME = (
    10  # Thời gian tối đa (tính bằng giây) mà robot được phép di chuyển trong mô phỏng
)
DT = 0.1  # Bước thời gian giữa các cập nhật vị trí mới của robot trong quá trình di chuyển
S = 1  # Ưu tiên của lực hấp dẫn so với lực đẩy từ các chướng ngại vật. Ảnh hưởng đến sự cân bằng giữa lực hấp dẫn và lực đẩy.
R = 7  # Bán kính của vùng ảnh hưởng của các chướng ngại vật. Các chướng ngại vật trong bán kính này sẽ tạo ra lực đẩy.
G = 1  # Độ ảnh hưởng của lực đẩy từ các chướng ngại vật. Ảnh hưởng đến sự cân bằng giữa lực hấp dẫn và lực đẩy.
reso = 0.5  # Độ phân giải của bản đồ tiềm năng, tức kích thước của mỗi ô lưới trên bản đồ tiềm năng
alpha = 1  # Hệ số này có thể được sử dụng trong các tính toán cụ thể, nhưng hiện tại không được sử dụng
beta = 1  # Hệ số này có thể được sử dụng trong các tính toán cụ thể, nhưng hiện tại không được sử dụng
AREA_WIDTH = 35.0  # Kích thước của khu vực mô phỏng, được sử dụng để xác định phạm vi của bản đồ tiềm năng
KP = 3.5  # Hằng số trong việc tính toán lực hấp dẫn từ mục tiêu. Ảnh hưởng đến sức mạnh của lực hấp dẫn
ETA = 100.0  # Hằng số trong việc tính toán lực đẩy từ các chướng ngại vật. Ảnh hưởng đến sức mạnh của lực đẩy


def calPose(x0, y0, x0g, y0g, obs_x, obs_y, start_x0, start_y0):
    """
    Tính toán vị trí mới của robot dựa trên phương pháp trường tiềm năng.

    Parameters:
        x0 (float): Tọa độ x hiện tại của robot.
        y0 (float): Tọa độ y hiện tại của robot.
        x0g (float): Tọa độ x của vị trí mục tiêu.
        y0g (float): Tọa độ y của vị trí mục tiêu.
        obs_x (list): Danh sách tọa độ x của các chướng ngại vật.
        obs_y (list): Danh sách tọa độ y của các chướng ngại vật.
        start_x0 (float): Tọa độ x ban đầu của robot.
        start_y0 (float): Tọa độ y ban đầu của robot.

    Returns:
        float: Tọa độ x mới của robot.
        float: Tọa độ y mới của robot.
    """
    # Khởi tạo các biến với vị trí ban đầu của robot
    x_cal = x0
    y_cal = y0

    # Tính toán bản đồ tiềm và truy xuất các giá trị cần thiết từ hàm calc_potential_field
    pmap, minx, miny = calcPotentialField(
        x0, y0, x0g, y0g, obs_x, obs_y, start_x0, start_y0
    )

    # Tính toán khoảng cách giữa vị trí hiện tại và mục tiêu
    d = np.hypot(x0 - x0g, y0 - y0g)

    # Tính toán chỉ số của ô lưới trên bản đồ tiềm tương ứng với vị trí hiện tại
    ix = round((x0 - minx) / reso)
    iy = round((y0 - miny) / reso)

    # Lấy danh sách các di chuyển có thể của robot
    motion = getMotionModel()

    # Nếu khoảng cách đến mục tiêu lớn hơn độ phân giải của bản đồ tiềm
    if d >= reso:
        # Khởi tạo giá trị tối thiểu của bản đồ tiềm
        minp = float("inf")
        minix, miniy = -1, -1

        # Lặp qua các di chuyển có thể
        for i, _ in enumerate(motion):
            # Tính toán chỉ số mới trên bản đồ tiềm
            inx = int(ix + motion[i][0])
            iny = int(iy + motion[i][1])

            # Kiểm tra xem chỉ số mới có nằm ngoài bản đồ tiềm không
            if inx >= len(pmap) or iny >= len(pmap[0]) or inx < 0 or iny < 0:
                # Nếu nằm ngoài, đặt giá trị tiềm năng thành vô cùng và in một thông báo
                p = float("inf")
                print("outside potential!")
            else:
                # Nếu không, lấy giá trị tiềm năng từ bản đồ tiềm
                p = pmap[inx][iny]

            # Tìm giá trị tiềm năng tối thiểu và lưu chỉ số tương ứng
            if minp > p:
                minp = p
                minix = inx
                miniy = iny

        # Cập nhật chỉ số của ô lưới với giá trị tiềm năng tối thiểu
        ix = minix
        iy = miniy

        # Tính toán lại vị trí mới của robot dựa trên chỉ số ô lưới và kích thước của ô lưới
        x_cal = ix * reso + minx
        y_cal = iy * reso + miny

    return x_cal, y_cal


def getMotionModel():
    """
    Định nghĩa danh sách các di chuyển có thể của robot.

    Returns:
        list: Danh sách các di chuyển có thể của robot.
    """
    # Khởi tạo danh sách các di chuyển có thể của robot
    motion = [
        [1, 0],  # Di chuyển sang phải
        [0, 1],  # Di chuyển lên trên
        [-1, 0],  # Di chuyển sang trái
        [0, -1],  # Di chuyển xuống dưới
        [-1, -1],  # Di chuyển chéo xuống bên phải
        [-1, 1],  # Di chuyển chéo xuống bên trái
        [1, -1],  # Di chuyển chéo lên bên phải
        [1, 1],
    ]  # Di chuyển chéo lên bên trái

    return motion  # Trả về danh sách các di chuyển có thể


def calcPotentialField(x0, y0, x0g, y0g, obs_x, obs_y, start_x0, start_y0):
    """
    Tính toán bản đồ trường tiềm.

    Parameters:
        x0 (float): Tọa độ x hiện tại của robot.
        y0 (float): Tọa độ y hiện tại của robot.
        x0g (float): Tọa độ x của vị trí mục tiêu.
        y0g (float): Tọa độ y của vị trí mục tiêu.
        obs_x (list): Danh sách tọa độ x của các chướng ngại vật.
        obs_y (list): Danh sách tọa độ y của các chướng ngại vật.
        start_x0 (float): Tọa độ x ban đầu của robot.
        start_y0 (float): Tọa độ y ban đầu của robot.

    Returns:
        list: Bản đồ trường tiềm.
        float: Tọa độ x tối thiểu của bản đồ trường tiềm.
        float: Tọa độ y tối thiểu của bản đồ trường tiềm.
    """
    # Xác định không gian chứa robot, mục tiêu và các chướng ngại vật
    minx = min(x0, x0g, min(obs_x), start_x0) - AREA_WIDTH / 2.0
    miny = min(y0, y0g, min(obs_y), start_y0) - AREA_WIDTH / 2.0
    maxx = max(x0, x0g, max(obs_x), start_x0) + AREA_WIDTH / 2.0
    maxy = max(y0, y0g, max(obs_y), start_y0) + AREA_WIDTH / 2.0

    # Tính toán số ô lưới trong mỗi chiều (chiều rộng và chiều cao)
    xw = int(round((maxx - minx) / reso))
    yw = int(round((maxy - miny) / reso))

    # Khởi tạo bản đồ trường tiềm và điểm bắt đầu của nó
    pmap = [[0.0 for i in range(yw)] for i in range(xw)]

    # Tính toán trường tiềm cho mỗi ô lưới trong không gian
    for ix in range(xw):
        x = ix * reso + minx
        for iy in range(yw):
            y = iy * reso + miny
            # Tính toán trường tiềm hấp dẫn từ mục tiêu
            ug = calcAttractivePotential(x, y, x0g, y0g)
            # Tính toán trường tiềm đẩy từ các chướng ngại vật
            uo = calcRepulsivePotential(x, y, obs_x, obs_y, R)
            # Kết hợp các trường tiềm từ cả hai loại
            uf = ug + uo
            # Gán trường tiềm cho ô lưới tương ứng
            pmap[ix][iy] = uf

    return pmap, minx, miny


def calcAttractivePotential(x, y, xg, yg):
    """
    Tính toán trường tiềm hấp dẫn từ mục tiêu.

    Parameters:
        x (float): Tọa độ x của điểm.
        y (float): Tọa độ y của điểm.
        xg (float): Tọa độ x của vị trí mục tiêu.
        yg (float): Tọa độ y của vị trí mục tiêu.

    Returns:
        float: Giá trị trường tiềm hấp dẫn.
    """
    # Tính toán khoảng cách Euclid từ điểm đến mục tiêu
    distance_to_goal = np.hypot(x - xg, y - yg)
    # Tính toán trường tiềm hấp dẫn dựa trên khoảng cách
    attractive_potential = KP * distance_to_goal
    return attractive_potential


def calcRepulsivePotential(x, y, obstacle_x, obstacle_y, rr):
    """
    Tính toán trường tiềm đẩy từ các chướng ngại vật.

    Parameters:
        x (float): Tọa độ x của điểm.
        y (float): Tọa độ y của điểm.
        obstacle_x (list): Danh sách tọa độ x của các chướng ngại vật.
        obstacle_y (list): Danh sách tọa độ y của các chướng ngại vật.
        rr (float): Phạm vi đẩy.

    Returns:
        float: Giá trị trường tiềm đẩy.
    """
    # Tìm chướng ngại vật gần nhất với điểm hiện tại
    minid = -1
    dmin = float("inf")
    for i, _ in enumerate(obstacle_x):
        d = np.hypot(x - obstacle_x[i], y - obstacle_y[i])
        if dmin >= d:
            dmin = d
            minid = i

    # Tính toán khoảng cách đến chướng ngại vật gần nhất
    dq = np.hypot(x - obstacle_x[minid], y - obstacle_y[minid])

    if dq <= rr:
        # Đảm bảo dq không bằng không
        if dq <= 0.1:
            dq = 0.1
        # Tính toán trường tiềm đẩy khi gần chướng ngại vật
        repulsive_potential = 0.5 * ETA * (1.0 / dq - 1.0 / rr) ** 2
    else:
        # Trường tiềm đẩy là không nếu không gần chướng ngại vật
        repulsive_potential = 0.0

    return repulsive_potential


def main(quantity_agent=6, save_demo=False):
    """
    Hàm chính để chạy mô phỏng.
    """
    time = 0.0
    # start
    # Tính toán tọa độ của start_positions trong một vòng tròn
    start_positions = {
        i: (
            10.0 + 10.0 * math.cos(2 * math.pi * i / quantity_agent),
            10.0 + 10.0 * math.sin(2 * math.pi * i / quantity_agent),
        )
        for i in range(quantity_agent)
    }

    # Tính toán tọa độ của goal_positions như điểm đối diện với start_positions
    goal_positions = {
        i: (20.0 - start_positions[i][0], 20.0 - start_positions[i][1])
        for i in range(quantity_agent)
    }

    for i in range(quantity_agent):
        globals()[f"x{i}"], globals()[f"y{i}"] = start_positions[i]
        globals()[f"x{i}g"], globals()[f"y{i}g"] = goal_positions[i]

    # Tạo danh sách màu sắc dựa trên quantity_agent
    colors = [cm.tab20(i) for i in range(quantity_agent)]

    fig, ax = plt.subplots()
    ims = []

    while SIM_TIME >= time:
        time += DT

        plt.gcf().canvas.mpl_connect(
            "key_release_event",
            lambda event: [exit(0) if event.key == "escape" else None],
        )

        artists = []
        for i in range(quantity_agent):
            globals()[f"x{i}"], globals()[f"y{i}"] = calPose(
                globals()[f"x{i}"],
                globals()[f"y{i}"],
                globals()[f"x{i}g"],
                globals()[f"y{i}g"],
                [globals()[f"x{j}"] for j in range(quantity_agent) if j != i],
                [globals()[f"y{j}"] for j in range(quantity_agent) if j != i],
                start_positions[i][0],
                start_positions[i][1],
            )

            artists.extend(
                plt.plot(globals()[f"x{i}"], globals()[f"y{i}"], ".", color=colors[i])
            )
            plt.annotate(
                f"{i + 1}", xy=(start_positions[i][0] - 1, start_positions[i][1])
            )

        ims.append(artists)

        plt.axis("equal")
        plt.grid(True)

    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)

    if save_demo:
        ani.save(f"Week4/demo/{quantity_agent}_agent.gif", writer="imagemagick")


if __name__ == "__main__":
    quantity_agents = [2, 4, 6, 8, 10, 20]
    for quantity_agent in quantity_agents:
        main(quantity_agent, save_demo=True)
