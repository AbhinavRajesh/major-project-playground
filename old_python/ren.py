import numpy as np
import trimesh
import pyrender
import matplotlib.pyplot as plt
from PIL import Image
import time
from math import sin, cos

scene = pyrender.Scene()
camera = pyrender.OrthographicCamera(xmag=1 , ymag=1)
box = trimesh.creation.box((0.5,0.5,0.5), np.eye(4))
box.visual.vertex_colors = np.random.uniform(size=box.vertices.shape)
nc = pyrender.Node(camera=camera)
box_m = pyrender.Mesh.from_trimesh(box, smooth=False)

box_nm = pyrender.Node(mesh=box_m)
scene.add_node(box_nm)
scene.add_node(nc)

theta = np.pi/4

arr = [[1,0,0,0.5],
       [0,1,0,0.5],
       [0,0,1,0.5],
       [0,0,0,1]]

roty = [[cos(theta),0,sin(theta),0],
       [0,1,0,0],
       [-sin(theta),0,cos(theta),0],
       [0,0,0,1]]

rotx = [[1,0,0,0],
        [0,cos(theta),sin(theta),0],
        [0,-sin(theta),cos(theta),0],
        [0,0,0,1]]

fin = np.matmul(np.matmul(roty,rotx),arr)
fin1 = [[0.70710678,-0.5,0.5,1],
 [0,0.70710678,0.70710678,1],
 [-0.70710678,-0.5,0.5,1],
 [0,0,0,1]]
scene.set_pose(nc, pose=np.array(fin1))

light = pyrender.SpotLight(color=(255,255,255), intensity=12.0,
                           innerConeAngle=np.pi/16.0,
                           outerConeAngle=np.pi/6.0)
scene.add(light, pose=fin1)

r = pyrender.OffscreenRenderer(1000, 1000)

# for i in range(500):
#    theta = theta + 0.05
#    color, depth = r.render(scene)

#    scene.set_pose(nc, pose=np.array([[1,0,0,.5],
#                                     [0,cos(theta),-sin(theta),.5],
#                                        [0,sin(theta),cos(theta),1],
#                                        [0,0,0,1]]))
#    im = Image.fromarray(color)
#    im.save(f"./test/your_file_{i}.jpeg")
i = 1
color, depth = r.render(scene)
im = Image.fromarray(color)
im.save(f"./test/your_file_{i}.jpeg")