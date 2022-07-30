import numpy as np
# import trimesh
# import pyrender
# import matplotlib.pyplot as plt
# from PIL import Image
# import time
# from math import sin, cos, acos, atan

def get_transform_matrix(p0,p1,p2,p3):
    dx1 = p1[0] - p0[0]
    dy1 = p1[1] - p0[1]
    dz1 = p1[2] - p0[2]

    dx2 = p3[0] - p2[0]
    dy2 = p3[1] - p2[1]
    dz2 = p3[2] - p2[2]

    d1 = np.sqrt(dx1**2 + dz1**2)
    d2 = np.sqrt(dx2**2 + dz2**2)

    l1 = np.sqrt(dx1**2 + dy1**2 + dz1**2)
    l2 = np.sqrt(dx2**2 + dy2**2 + dz2**2)


    F = d1**2 * p0[1] - dy1 * (p0[0]*dx1 + p0[2]*dz1)
    G = p0[0]*dz1 - p0[2]*dx1
    H = p0[1]*dy1 + p0[0]*dx1 + p0[2]*dz1
    I = dy1*dy2 + d1*d2
    X = dx1*dx2
    Y = dy1*dy2
    Z = dz1*dz2
    D = d1*d2
    L = l1*l2
    U = 1/(l1**2 * d1 * d2)

    return [
        [U*(Z*L + X*I), dx2*d1*U*(dy1*d2 - dy2*d1), U*(dz1*dx2*I - dz2*dx1*L), U*(dz2*G*L + dx2*(D*H - dy1*F)) + p2[0]],
        [-dx1*d2*U*(dy1*d2 + dy2*d1), D*U*I, dz1*d2*U*(dy2*d1 - dy1*d2), U*d2*(F*d2 + dy2*d1*H) + p2[1]],
        [U*(dz2*dx1*I - dx2*dz1*L), dz2*d1*U*(dy1*d2 - dy2*d1), U*(X*L + Z*I), U*(-dx1*L*G + dz2*(D*H - dy1*F)) + p2[2]],
        [0, 0, 0, 1]
    ]

p0 = [2, 4, 1, 1]
p1 = [4, 1, 8, 1]
p2 = [-4, 7, 2, 1]
p3 = [2, 5, 8, 1]

mat = get_transform_matrix(p0, p1, p2, p3)
print(mat)
# p0 = [[2], [4], [1], [1]]
# p1 = [[4], [1], [8], [1]]

p_2 = np.dot(mat, p0)
p_3 = np.dot(mat, p1)

print(p2, p3, p_2, p_3)