import numpy as np
# import trimesh
# import pyrender
# import matplotlib.pyplot as plt
# from PIL import Image
# import time
from math import sin, cos, acos, atan, asin

def translate(tx,ty,tz):
    return [[1,0,0,tx],
            [0,1,0,ty],
            [0,0,1,tz],
            [0,0,0,1]]

def scale(sx,sy,sz):
    return [[sx,0,0,0],
            [0,sy,0,0],
            [0,0,sz,0],
            [0,0,0,1]]

def xrotate(theta):
    return [[1,0,0,0],
            [0,cos(theta),-sin(theta),0],
            [0,sin(theta),cos(theta),0],
            [0,0,0,1]]

def yrotate(theta):
    return [[cos(theta),0,sin(theta),0],
            [0,1,0,0],
            [-sin(theta),0,cos(theta),0],
            [0,0,0,1]]

def zrotate(theta):
    return [[cos(theta),-sin(theta),0,0],
            [sin(theta),cos(theta),0,0],
            [0,0,1,0],
            [0,0,0,1]]

p0 = [2, 4, 1, 1]
p1 = [4, 1, 8, 1]
p2 = [-4, 7, 2, 1]
p3 = [2, 5, 8, 1]

dx1 = p1[0] - p0[0]
dy1 = p1[1] - p0[1]
dz1 = p1[2] - p0[2]

dx2 = p3[0] - p2[0]
dy2 = p3[1] - p2[1]
dz2 = p3[2] - p2[2]

theta1 = atan(dx1/dz1)
theta2 = atan(dy1/np.sqrt(dx1**2 + dz1**2))

theta3 = atan(dy2/np.sqrt(dx2**2 + dz2**2))
theta4 = atan(dx2/dz2)

l1 = np.sqrt(dx1**2 + dy1**2 + dz1**2)
l2 = np.sqrt(dx2**2 + dy2**2 + dz2**2)

f = l2/l1

# theta1 = asin(dx1/np.sqrt(dx1**2 + dz1**2))
# print(theta1)

a1 = translate(-p0[0],-p0[1],-p0[2])
a2 = yrotate(-theta1)
a3 = xrotate(theta2)
a4 = scale(f,f,f)
a5 = xrotate(-theta3)
a6 = yrotate(theta4)
a7 = translate(p2[0],p2[1],p2[2])

# mat1 = np.matmul(a1,p1)
# print(mat1)
# mat2 = np.matmul(a2,mat1)
# print(mat2)
# mat3 = np.matmul(a3,mat2)
# print(mat3)
# mat4 = np.matmul(a4,mat3)
# mat5 = np.matmul(a5,mat4)
# mat6 = np.matmul(a6,mat5)
# mat7 = np.matmul(a7,mat6)

mat2 = np.matmul(a7,np.matmul(a6,np.matmul(a5,np.matmul(a4,np.matmul(a3,np.matmul(a2,a1))))))

# mat1 = np.matmul(a1, a2)
print(p3)
# mat3 = np.matmul(mat2, mat1)
mat4 = np.matmul(mat2, p1)

print(mat4)