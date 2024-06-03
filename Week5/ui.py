import pygame
from constants import *
from tools import *

class Button:
    def __init__(self, text, position = (Width-230, 600) , w = 100, h= 50, border=10, color = (0, 0, 0), borderColor = (64, 123, 158)):
        """
        Khởi tạo một đối tượng Button với các tham số được cung cấp.

        Args:
            text (str): Đoạn văn bản được hiển thị trên nút.
            position (tuple, optional): Vị trí của góc trên bên trái của nút. Mặc định là (Width-230, 600).
            w (int, optional): Chiều rộng của nút. Mặc định là 100.
            h (int, optional): Chiều cao của nút. Mặc định là 50.
            border (int, optional): Độ dày của viền của nút. Mặc định là 10.
            color (tuple, optional): Màu của nút. Mặc định là (0, 0, 0).
            borderColor (tuple, optional): Màu của viền của nút. Mặc định là (64, 123, 158).
        """
        self.text = text
        self.position = position
        self.w = w
        self.h = h
        self.border = border
        self.temp = color
        self.color = color
        self.borderColor = borderColor
        self.font = 'freesansbold.ttf'
        self.fontSize = 25
        self.textColor = (255, 255, 255)
        self.state = False
        self.action = None

    def HandleMouse(self, HoverColor = (100, 100, 100)):
        """
        Xử lý sự kiện khi con trỏ chuột di chuyển qua nút.

        Args:
            HoverColor (tuple, optional): Màu khi nút được di chuột qua. Mặc định là (100, 100, 100).
        """
        m = pygame.mouse.get_pos()
        self.state = False
        if m[0] >= self.position[0] and m[0] <= self.position[0] + self.w:
            if m[1] >= self.position[1] and m[1] <= self.position[1] + self.h:
                self.color = HoverColor
                if pygame.mouse.get_pressed()[0]:
                    self.color = (200, 200, 200)
                    if self.action == None:
                        self.state = True
            else:
                self.color = self.temp
        else:
            self.color = self.temp


    def Render(self, screen):
        """
        Hiển thị nút trên màn hình.

        Args:
            screen (pygame.Surface): Bề mặt màn hình để hiển thị nút.
        """
        self.HandleMouse()
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.textColor)
        textRect = text.get_rect()
        textRect.center = (self.position[0]+self.w//2, self.position[1]+self.h//2)
        if self.border > 0:
            pygame.draw.rect(screen, self.borderColor, pygame.Rect(self.position[0] - self.border//2, self.position[1] - self.border//2, self.w + self.border, self.h + self.border))
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))

        screen.blit(text, textRect)

class Panel:
    def __init__(self, position = (Width-350, 100), w= 345, h= 500, color=(8, 3, 12), alpha=128):
        """
        Khởi tạo một đối tượng Panel với các tham số được cung cấp.

        Args:
            position (tuple, optional): Vị trí của góc trên bên trái của bảng. Mặc định là (Width-350, 100).
            w (int, optional): Chiều rộng của bảng. Mặc định là 345.
            h (int, optional): Chiều cao của bảng. Mặc định là 500.
            color (tuple, optional): Màu của bảng. Mặc định là (8, 3, 12).
            alpha (int, optional): Độ trong suốt của bảng. Mặc định là 128.
        """
        self.position = position
        self.w = w
        self.h = h
        self.color = color
        self.alpha = alpha

    def Render(self, screen):
        """
        Hiển thị bảng trên màn hình.

        Args:
            screen (pygame.Surface): Bề mặt màn hình để hiển thị bảng.
        """
        s = pygame.Surface((self.w, self.h))
        s.set_alpha(self.alpha)
        s.fill(self.color)
        screen.blit(s, (self.position[0], self.position[1]))
        # pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))

class ToggleButton:
    def __init__(self, position= ((Width-200, 400)), w = 30, h=30, state=False, color=(40, 40, 10), activeColor=(240, 140, 60)):
        """
        Khởi tạo một đối tượng ToggleButton với các tham số được cung cấp.

        Args:
            position (tuple, optional): Vị trí của góc trên bên trái của nút. Mặc định là (Width-200, 400).
            w (int, optional): Chiều rộng của nút. Mặc định là 30.
            h (int, optional): Chiều cao của nút. Mặc định là 30.
            state (bool, optional): Trạng thái ban đầu của nút. Mặc định là False.
            color (tuple, optional): Màu của nút. Mặc định là (40, 40, 10).
            activeColor (tuple, optional): Màu của nút khi được kích hoạt. Mặc định là (240, 140, 60).
        """
        self.position = position
        self.w = w
        self.h = h
        self.clicked = False
        self.state = state
        self.temp = (activeColor, color)
        self.activeColor = activeColor
        self.color = color

    def HandleMouse(self, HoverColor = (150, 120, 40)):
        """
        Xử lý sự kiện khi con trỏ chuột di chuyển qua nút và nút được nhấn.

        Args:
            HoverColor (tuple, optional): Màu khi nút được di chuột qua. Mặc định là (150, 120, 40).
        """
        m = pygame.mouse.get_pos()

        if m[0] >= self.position[0] and m[0] <= self.position[0] + self.w:
            if m[1] >= self.position[1] and m[1] <= self.position[1] + self.h:
                self.color = HoverColor
                self.activeColor = HoverColor
                if self.clicked:
                    self.state = not self.state
                    self.color = (255, 255, 255)
            else:
                self.color = self.temp[1]
                self.activeColor =self.temp[0]
        else:
            self.color = self.temp[1]
            self.activeColor =self.temp[0]

    def Render(self, screen, clicked):
        """
        Hiển thị nút trên màn hình và xác định trạng thái của nút.

        Args:
            screen (pygame.Surface): Bề mặt màn hình để hiển thị nút.
            clicked (bool): Biến xác định xem nút có được nhấn hay không.

        Returns:
            bool: Trạng thái của nút.
        """
        self.HandleMouse()
        self.clicked = clicked
        if self.state == True:
            pygame.draw.rect(screen, self.activeColor, pygame.Rect(self.position[0], self.position[1], self.w, self.h))
        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))
        return self.state

class TextUI:
    def __init__(self,text, position, fontColor):
        """
        Khởi tạo một đối tượng TextUI với các tham số được cung cấp.

        Args:
            text (str): Đoạn văn bản được hiển thị.
            position (tuple): Vị trí của góc trên bên trái của văn bản.
            fontColor (tuple): Màu của văn bản.
        """
        self.position = position
        self.text = text
        self.font = 'freesansbold.ttf'
        self.fontSize = 18
        self.fontColor = fontColor

    def Render(self, screen):
        """
        Hiển thị văn bản trên màn hình.

        Args:
            screen (pygame.Surface): Bề mặt màn hình để hiển thị văn bản.
        """
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.fontColor)
        textRect = text.get_rect()
        textRect.center = (self.position[0], self.position[1])
        screen.blit(text, textRect)

class DigitInput:
    def __init__(self,startingValue, position = (Width-320, 100), w= 300, h= 600, color=(8, 3, 12)):
        """
        Khởi tạo một đối tượng DigitInput với các tham số được cung cấp.

        Args:
            startingValue (int): Giá trị ban đầu của ô nhập số.
            position (tuple, optional): Vị trí của góc trên bên trái của ô nhập số. Mặc định là (Width-320, 100).
            w (int, optional): Chiều rộng của ô nhập số. Mặc định là 300.
            h (int, optional): Chiều cao của ô nhập số. Mặc định là 600.
            color (tuple, optional): Màu của ô nhập số. Mặc định là (8, 3, 12).
        """
        self.position = position
        self.text = str(startingValue)
        self.fontColor = (255, 255, 255)
        self.fontSize = 18
        self.font = 'freesansbold.ttf'
        self.w = w
        self.h = h
        self.color = color
        self.value  = int(self.text)
        self.hoverEnter = False

    def Check(self, backspace,val):
        """
        Kiểm tra sự kiện nhấn phím và cập nhật giá trị của ô nhập số.

        Args:
            backspace (bool): Biến xác định xem phím backspace có được nhấn hay không.
            val (str): Giá trị của phím được nhấn.
        """
        if self.hoverEnter == True:
            if backspace == True:

                if len(str(self.value)) <= 0 or len(str(self.value))-1 <= 0:
                    self.value = 0
                else:
                    self.value = int(str(self.value)[:-1])

            else:
                if self.text.isdigit():
                    self.value = int(str(self.value) + str(self.text))
                else:
                    for el in self.text:
                        if el.isdigit() != True:
                            self.text = self.text.replace(el, "")
        backspace == False
        self.text = ""

    def updateText(self, val, pressed):
        """
        Cập nhật văn bản khi người dùng nhập giá trị.

        Args:
            val (str): Giá trị của phím được nhấn.
            pressed (bool): Biến xác định xem một phím đã được nhấn hay không.
        """
        m = pygame.mouse.get_pos()
        if m[0] >= self.position[0] and m[0] <= self.position[0] + self.w:
            if m[1] >= self.position[1] and m[1] <= self.position[1] + self.h:
                self.hoverEnter = True
                if pressed == True:
                    self.text += val
            else:
                self.hoverEnter = False
                val = ""
        else:
            self.hoverEnter = False
            val = ""

    def Render(self, screen, val, backspace, pressed):
        """
        Hiển thị ô nhập số trên màn hình và cập nhật giá trị của ô nhập số.

        Args:
            screen (pygame.Surface): Bề mặt màn hình để hiển thị ô nhập số.
            val (str): Giá trị của phím được nhấn.
            backspace (bool): Biến xác định xem phím backspace có được nhấn hay không.
            pressed (bool): Biến xác định xem một phím đã được nhấn hay không.
        """
        self.updateText(val, pressed)
        self.Check(backspace, val)
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(str(self.value), True, self.fontColor)
        textRect = text.get_rect()
        textRect.center = (self.position[0]+self.w//2, self.position[1]+self.h//2)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))
        screen.blit(text, textRect)

class Slider:
    def __init__(self,x, y, val, min1, max1, length, h, max=500):
        """
        Khởi tạo một đối tượng Slider với các tham số được cung cấp.

        Args:
            x (int): Tọa độ x của điểm gốc trái của slider.
            y (int): Tọa độ y của điểm gốc trái của slider.
            val (float): Giá trị ban đầu của slider.
            min1 (float): Giá trị tối thiểu của slider.
            max1 (float): Giá trị tối đa của slider.
            length (int): Chiều dài của slider.
            h (int): Chiều cao của slider.
            max (int, optional): Giá trị tối đa mà slider có thể đạt được. Mặc định là 500.
        """
        self.value = val
        self.x = x
        self.y = y
        self.h = h
        self.min1 = min1
        self.max1 = max1
        self.length = length
        self.lineColor = (20, 10, 20)
        self.rectradius = 10
        self.temp_radius = self.rectradius
        self.rectColor = (255, 255, 255)
        self.v = 0.4
        self.temp = self.lineColor
        self.max = max

    def Calculate(self, val):
        """
        Tính toán giá trị của slider dựa trên vị trí của con trỏ chuột.

        Args:
            val (int): Vị trí của con trỏ chuột trên slider.
        """
        self.v = translate(val, 0, self.length, 0, 1)
        self.value = self.v * self.max

    def HandleMouse(self):
        """
        Xử lý sự kiện khi con trỏ chuột di chuyển trên slider.
        """
        mx, my = pygame.mouse.get_pos()

        if mx >= self.x and mx <= self.x + self.length:
            if my >= self.y and my <= self.y + self.h:
                self.rectradius = 15
                if pygame.mouse.get_pressed()[0]:
                    self.Calculate(mx - self.x)
            else:
                self.lineColor = self.temp
                self.rectradius = self.temp_radius
        else:
            self.lineColor = self.temp
            self.rectradius = self.temp_radius

    def Render(self,screen):
        """
        Hiển thị slider trên màn hình và trả về giá trị hiện tại của slider.

        Args:
            screen (pygame.Surface): Bề mặt màn hình để hiển thị slider.

        Returns:
            float: Giá trị hiện tại của slider.
        """
        self.HandleMouse()
        pygame.draw.rect(screen, self.lineColor, pygame.Rect(self.x, self.y, self.length, self.h))
        x = int((self.v * self.length) + self.x)
        pygame.draw.rect(screen, self.rectColor, pygame.Rect(self.x, self.y, int( self.v * self.length), self.h))
        pygame.draw.circle(screen, (130, 213, 151), (x, self.y + (self.rectradius/2)), self.rectradius)
        return self.value
