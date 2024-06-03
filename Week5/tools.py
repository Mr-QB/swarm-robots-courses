from math import sqrt, atan2
import colorsys

NEIGHBORHOOD_RADIUS = 40

class Vector:
    """
    Lớp đại diện cho một vector 2D.

    Attributes:
        x (float): Tọa độ x của vector.
        y (float): Tọa độ y của vector.
    """

    def __init__(self, x=0, y=0):
        """
        Khởi tạo một đối tượng Vector với các tọa độ x và y đã cho.

        Parameters:
            x (float): Tọa độ x của vector. Mặc định là 0.
            y (float): Tọa độ y của vector. Mặc định là 0.
        """
        self.x = x
        self.y = y

    def __mul__(self, a):
        """
        Nhân vector với một số vô hướng.

        Parameters:
            a (float): Giá trị số vô hướng.

        Returns:
            Vector: Vector kết quả sau khi nhân.
        """
        self.x = self.x * a
        self.y = self.y * a
        return self

    def __add__(self, a):
        """
        Cộng một vector khác vào vector này.

        Parameters:
            a (Vector): Vector cần cộng.

        Returns:
            Vector: Vector kết quả sau khi cộng.
        """
        self.x = self.x + a.x
        self.y = self.y + a.y
        return self

    def __sub__(self, a):
        """
        Trừ một vector khác từ vector này.

        Parameters:
            a (Vector): Vector cần trừ.

        Returns:
            Vector: Vector kết quả sau khi trừ.
        """
        self.x = self.x - a.x
        self.y = self.y - a.y
        return self

    def __truediv__(self, a):
        """
        Chia vector cho một số vô hướng.

        Parameters:
            a (float): Giá trị số vô hướng.

        Returns:
            Vector: Vector kết quả sau khi chia.
        """
        self.x = self.x / a
        self.y = self.y / a
        return self

    def add(self, a):
        """
        Cộng một vector khác vào vector này.

        Parameters:
            a (Vector): Vector cần cộng.
        """
        self.x = self.x + a.x
        self.y = self.y + a.y

    def parseToInt(self):
        """
        Chuyển đổi các tọa độ của vector thành số nguyên.

        Returns:
            tuple: Bộ chứa các tọa độ nguyên (x, y).
        """
        return (int(self.x), int(self.y))

    def magnitude(self):
        """
        Tính toán độ lớn (độ dài) của vector.

        Returns:
            float: Độ lớn của vector.
        """
        return sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        """
        Chuẩn hóa vector (đưa độ lớn về bằng 1).
        """
        mag = self.magnitude()
        if not (mag == 0 ):
            self = self/mag

    def Normalize(self):
        """
        Trả về một bản sao đã được chuẩn hóa của vector mà không làm thay đổi vector ban đầu.

        Returns:
            Vector: Vector đã được chuẩn hóa.
        """
        mag = self.magnitude()
        if mag != 0:
            return Vector(self.x/mag, self.y/mag)
        else:
            return Vector(1, 1)

    def heading(self):
        """
        Tính toán góc (heading) của vector theo radian.

        Returns:
            float: Góc của vector theo radian.
        """
        angle = atan2(self.y, self.x)
        return angle

    def limit(self, max_length):
        """
        Giới hạn độ lớn của vector thành một giá trị tối đa.

        Parameters:
            max_length (float): Độ lớn tối đa cho phép của vector.
        """
        squared_mag = self.magnitude() * self.magnitude()
        if squared_mag > (max_length * max_length):
            self.x = self.x/sqrt(squared_mag)
            self.y = self.y/sqrt(squared_mag)
            self.x = self.x * max_length
            self.y = self.y * max_length

    def reset(self, x=0, y=0):
        """
        Thiết lập lại vector đến một vị trí mới.

        Parameters:
            x (float): Tọa độ x mới. Mặc định là 0.
            y (float): Tọa độ y mới. Mặc định là 0.
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Biểu diễn dạng chuỗi của đối tượng Vector.

        Returns:
            str: Biểu diễn dạng chuỗi của vector.
        """
        return f'vector-> x:{self.x}, y:{self.y}'


def getDistance(v1, v2):
    """
    Tính khoảng cách Euclidean giữa hai vector.

    Parameters:
        v1 (Vector): Vector thứ nhất.
        v2 (Vector): Vector thứ hai.

    Returns:
        float: Khoảng cách Euclidean giữa hai vector.
    """
    return sqrt((v2.x - v1.x)*(v2.x - v1.x) + (v2.y -v1.y)*(v2.y - v1.y))

def AddVectors(v1, v2):
    """
    Cộng hai vector lại với nhau.

    Parameters:
        v1 (Vector): Vector thứ nhất.
        v2 (Vector): Vector thứ hai.

    Returns:
        Vector: Vector kết quả sau khi cộng.
    """
    return Vector(v1.x + v2.x, v1.y + v2.y)

def translate(value, min1, max1, min2, max2):
    """
    Dịch một giá trị từ một phạm vi sang một phạm vi khác.

    Parameters:
        value (float): Giá trị cần dịch.
        min1 (float): Giá trị tối thiểu của phạm vi ban đầu.
        max1 (float): Giá trị tối đa của phạm vi ban đầu.
        min2 (float): Giá trị tối thiểu của phạm vi mới.
        max2 (float): Giá trị tối đa của phạm vi mới.

    Returns:
        float: Giá trị đã được dịch.
    """
    return min2 + (max2 - min2)* ((value-min1)/(max1-min1))

def hsv_to_rgb(h, s, v):
    """
    Chuyển đổi không gian màu HSV sang không gian màu RGB.

    Parameters:
        h (float): Giá trị Hue (0-1).
        s (float): Giá trị Saturation (0-1).
        v (float): Giá trị Value (độ sáng) (0-1).

    Returns:
        tuple: Bộ màu RGB.
    """
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def SubVectors(v1, v2):
    """
    Trừ một vector từ một vector khác.

    Parameters:
        v1 (Vector): Vector thứ nhất.
        v2 (Vector): Vector thứ hai.

    Returns:
        Vector: Vector kết quả sau khi trừ.
    """
    return Vector(v1.x - v2.x, v1.y - v2.y)
