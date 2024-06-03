import pygame
from boid import Boid
from tools import Vector
import math
import random
from matrix import *
from constants import *
from uiParameters import *

pygame.init()
window = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()
fps = 60

scale = 40  # Đặt tỉ lệ mặc định cho bán kính boid
Distance = 5  # Khoảng cách mặc định giữa các boid
speed = 0.0005  # Tốc độ mặc định của sự thay đổi màu sắc

flock = []  # Danh sách chứa các boid
n = 50  # Số lượng boid mặc định

for i in range(n):
    # Tạo ngẫu nhiên vị trí cho mỗi boid trong phạm vi màn hình
    flock.append(Boid(random.randint(20, Width-20), random.randint(20, Height-20)))

textI = "10"  # Giá trị mặc định cho ô nhập số
reset = False
SpaceButtonPressed = False
backSpace = False
keyPressed = False
showUI = False
clicked = False
run = True
while run:
    clock.tick(fps)
    window.fill((10, 10, 15))  # Xóa màn hình và đặt màu nền

    n = numberInput.value  # Lấy giá trị số lượng boid từ ô nhập số
    scale = sliderScale.value  # Lấy giá trị tỉ lệ bán kính từ thanh trượt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_r:
                reset = True
            if event.key == pygame.K_SPACE:
                SpaceButtonPressed = True

            textI = pygame.key.name(event.key)
            keyPressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                backSpace = True
            if event.key == pygame.K_u:
                showUI = not showUI

    if reset == True or resetButton.state == True:
        # Khởi tạo lại danh sách boid nếu nhấn nút "Reset" hoặc biến reset được đặt thành True
        flock = []
        for i in range(n):
            flock.append(Boid(random.randint(20, Width-20), random.randint(20, Height-20)))
        reset = False

    for boid in flock:
        # Cập nhật các giá trị của boid
        boid.toggles = {"separation": toggleSeparation.state, "alignment": toggleAlignment.state, "cohesion": toggleCohesion.state}
        boid.values = {"separation": separationInput.value/100, "alignment": alignmentInput.value/100, "cohesion": cohesionInput.value/100}
        boid.radius = scale
        boid.limits(Width, Height)  # Giới hạn boid trong màn hình
        boid.behaviour(flock)  # Áp dụng các hành vi của boid
        boid.update()  # Cập nhật vị trí của boid
        boid.hue += speed  # Thay đổi màu sắc của boid
        boid.Draw(window, Distance, scale)  # Vẽ boid lên cửa sổ

    if showUI == True:
        # Hiển thị giao diện người dùng nếu showUI được đặt thành True
        panel.Render(window)
        resetButton.Render(window)
        Behaviours.Render(window)
        Separation.Render(window)
        Alignment.Render(window)
        Cohesion.Render(window)
        SeparationValue.Render(window)
        AlignmentValue.Render(window)
        CohesionValue.Render(window)
        NumberOfBoids.Render(window)
        ScaleText.Render(window)
        toggleSeparation.Render(window, clicked)
        toggleAlignment.Render(window, clicked)
        toggleCohesion.Render(window, clicked)
        separationInput.Render(window, textI, backSpace, keyPressed)
        alignmentInput.Render(window, textI, backSpace, keyPressed)
        cohesionInput.Render(window, textI, backSpace, keyPressed)
        numberInput.Render(window, textI, backSpace, keyPressed)
        sliderScale.Render(window)
    else:
        UItoggle.Render(window)  # Hiển thị thông báo để bật/tắt giao diện người dùng

    backSpace = False
    keyPressed = False
    pygame.display.flip()  # Cập nhật màn hình
    clicked = False
pygame.quit()
