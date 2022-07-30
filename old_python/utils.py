import numpy as np
from math import sin, cos, acos, atan

def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def get_angles(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    c = p1[2] - p2[2]

    l = np.sqrt(a * a + b * b + c * c)

    x = acos(a / l)
    y = acos(b / l)
    z = acos(c / l)

    return x, y, z


def get_euler_rot_matrix(x, y, z):
    cx = cos(x)
    cy = cos(y)
    cz = cos(z)

    sx = sin(x)
    sy = sin(y)
    sz = sin(z)

    return np.array([[cy * cz, (sx * sy * cz) - (cx * sz), (cx * sy * sz) - (sx * cz), 0],
                     [cy * sz, (sx * sy * sz) - (cx * cz), (cx * sy * sz) - (sx * cz), 0],
                     [-sy, sx * cy, cx * cy, 0],
                     [0, 0, 0, 1]])


def get_y_rotation_matrix(theta):
    return np.array([[np.cos(theta), 0, -np.sin(theta), 0],
                     [0, 1, 0, 0],
                     [np.sin(theta), 0, np.cos(theta), 0],
                     [0, 0, 0, 1]])


def get_translation_matrix(tx, ty, tz):
    return [[1, 0, 0, tx],
            [0, 1, 0, ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1]]


def get_scale_matrix(sx, sy, sz):
    return [[sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]]


def get_x_rotation_matrix(theta):
    return np.array([[1, 0, 0, 0],
                     [0, cos(theta), -sin(theta), 0],
                     [0, sin(theta), cos(theta), 0],
                     [0, 0, 0, 1]])


def get_z_rotation_matrix(theta):
    return np.array([[cos(theta), -sin(theta), 0, 0],
                     [sin(theta), cos(theta), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
