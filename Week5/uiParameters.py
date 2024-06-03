from ui import *

panel = Panel()  # Khởi tạo một bảng điều khiển
panel.color = (0, 0, 0)  # Đặt màu nền của bảng điều khiển là đen
resetButton = Button("Reset")  # Khởi tạo một nút "Reset"

Behaviours = TextUI(
    "BEHAVIOURS", (Width - 180, 120), (255, 255, 255)
)  # Hiển thị tiêu đề "BEHAVIOURS" tại vị trí (Width-180, 120) với màu trắng
UItoggle = TextUI(
    "Press 'U' to show parameter panel", (Width - 180, 120), (55, 120, 255)
)  # Hiển thị thông báo "Press 'U' to show parameter panel" tại vị trí (Width-180, 120) với màu xanh dương

Separation = TextUI(
    "Separation: ", (Width - 245, 180), (255, 255, 255)
)  # Hiển thị tiêu đề "Separation: " tại vị trí (Width-245, 180) với màu trắng
Alignment = TextUI(
    "Alignment: ", (Width - 245, 220), (255, 255, 255)
)  # Hiển thị tiêu đề "Alignment: " tại vị trí (Width-245, 220) với màu trắng
Cohesion = TextUI(
    "Cohesion: ", (Width - 245, 260), (255, 255, 255)
)  # Hiển thị tiêu đề "Cohesion: " tại vị trí (Width-245, 260) với màu trắng

SeparationValue = TextUI(
    "separationValue: ", (Width - 245, 315), (255, 255, 255)
)  # Hiển thị tiêu đề "separationValue: " tại vị trí (Width-245, 315) với màu trắng
AlignmentValue = TextUI(
    "alignmentValue: ", (Width - 245, 365), (255, 255, 255)
)  # Hiển thị tiêu đề "alignmentValue: " tại vị trí (Width-245, 365) với màu trắng
CohesionValue = TextUI(
    "cohesionValue: ", (Width - 245, 415), (255, 255, 255)
)  # Hiển thị tiêu đề "cohesionValue: " tại vị trí (Width-245, 415) với màu trắng
NumberOfBoids = TextUI(
    "Number of Boids: ", (Width - 245, 465), (255, 255, 255)
)  # Hiển thị tiêu đề "Number of Boids: " tại vị trí (Width-245, 465) với màu trắng
ScaleText = TextUI(
    "Boid-Scale (radius): ", (Width - 200, 520), (255, 255, 255)
)  # Hiển thị tiêu đề "Boid-Scale (radius): " tại vị trí (Width-200, 520) với màu trắng

toggleSeparation = ToggleButton(
    (Width - 160, 170), 20, 20, True
)  # Khởi tạo một nút toggle "Separation" tại vị trí (Width-160, 170) với kích thước 20x20 và trạng thái ban đầu là True
toggleAlignment = ToggleButton(
    (Width - 160, 210), 20, 20, True
)  # Khởi tạo một nút toggle "Alignment" tại vị trí (Width-160, 210) với kích thước 20x20 và trạng thái ban đầu là True
toggleCohesion = ToggleButton(
    (Width - 160, 250), 20, 20, True
)  # Khởi tạo một nút toggle "Cohesion" tại vị trí (Width-160, 250) với kích thước 20x20 và trạng thái ban đầu là True

separationInput = DigitInput(
    10, (Width - 160, 300), 80, 30
)  # Khởi tạo một ô nhập số "Separation" với giá trị ban đầu là 10, tại vị trí (Width-160, 300) với kích thước 80x30
alignmentInput = DigitInput(
    10, (Width - 160, 350), 80, 30
)  # Khởi tạo một ô nhập số "Alignment" với giá trị ban đầu là 10, tại vị trí (Width-160, 350) với kích thước 80x30
cohesionInput = DigitInput(
    10, (Width - 160, 400), 80, 30
)  # Khởi tạo một ô nhập số "Cohesion" với giá trị ban đầu là 10, tại vị trí (Width-160, 400) với kích thước 80x30
numberInput = DigitInput(
    100, (Width - 160, 450), 80, 30
)  # Khởi tạo một ô nhập số "Number of Boids" với giá trị ban đầu là 100, tại vị trí (Width-160, 450) với kích thước 80x30

sliderScale = Slider(
    Width - 280, 550, 40, 0, 100, 180, 10, 80
)  # Khởi tạo một thanh trượt để chọn "Boid-Scale (radius)" tại vị trí (Width-280, 550) với kích thước thanh 40x180 và giá trị ban đầu là 80
