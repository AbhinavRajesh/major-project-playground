from hand import Hand, hand_coords
import pyrender
import trimesh
import numpy as np
from PIL import Image
from utils import *

i = 0


def take_snapshot(tag=''):
    global i
    color, _ = renderer.render(scene)
    im = Image.fromarray(color)
    im.save(f"./test/snapshot_{i}_{tag}.jpeg")
    print(f"Taking snapshot {i}. {tag}")
    i += 1


scene = pyrender.Scene()

cube_trimesh = trimesh.creation.box(extents=[0.3, 0.3, 0.3])
cube_trimesh.visual.face_colors = [0.5, 0, 0, 1]
# cube_trimesh.visual.vertex_colors = np.random.uniform(size=cube_trimesh.vertices.shape)
cube_mesh = pyrender.Mesh.from_trimesh(cube_trimesh, smooth=False)

cube_node = scene.add(cube_mesh)

camera = pyrender.OrthographicCamera(xmag=1, ymag=1)
camera_node = pyrender.Node(camera=camera)
scene.add_node(camera_node)


arr = [[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 1.],
       [0., 0., 0., 1.]]
scene.set_pose(camera_node, pose=np.array(arr))

light = pyrender.SpotLight(color=(255, 255, 255), intensity=12.0,
                           innerConeAngle=0,
                           outerConeAngle=np.pi / 2.0)
scene.add(light, pose=arr)

renderer = pyrender.OffscreenRenderer(500, 500)

take_snapshot()

translation_matrix = np.array([[1, 0, 0, 0.1],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])

mat1 = get_translation_matrix(0.5, )
rotation_matrix = get_y_rotation_matrix(np.pi/16)
for _ in range(20):
    pose = np.matmul(cube_node.matrix, rotation_matrix)
    scene.set_pose(cube_node, pose=pose)
    take_snapshot()

