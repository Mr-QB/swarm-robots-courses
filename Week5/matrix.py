import math

def matrix_multiplication(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)
    
    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for x in range(rows_a):
            for y in range(columns_b):
                sum = 0
                for k in range(columns_a):
                    sum += a[x][k] * b[k][y]
                result_matrix[x][y] = sum
        return result_matrix

    else:
        print("columns of the first matrix must be equal to the rows of the second matrix")
        return None


def rotationX(angle):
    """
    Ma trận quay quanh trục X.

    Parameters:
        angle (float): Góc quay theo radian.

    Returns:
        list: Ma trận quay 3x3.
    """
    return [[1, 0, 0],
            [0, math.cos(angle), -math.sin(angle)],
            [0, math.sin(angle), math.cos(angle)]]

def rotationY(angle):
    """
    Ma trận quay quanh trục Y.

    Parameters:
        angle (float): Góc quay theo radian.

    Returns:
        list: Ma trận quay 3x3.
    """
    return [[math.cos(angle), 0, -math.sin(angle)],
            [0, 1, 0],
            [math.sin(angle), 0, math.cos(angle)]]

def rotationZ(angle):
    """
    Ma trận quay quanh trục Z.

    Parameters:
        angle (float): Góc quay theo radian.

    Returns:
        list: Ma trận quay 3x3.
    """
    return [[math.cos(angle), -math.sin(angle), 0],
            [math.sin(angle), math.cos(angle), 0],
            [0, 0 ,1]]
