import numpy as np
import trimesh
import pyrender
from PIL import Image
from math import sin, cos, acos, atan
from utils import *

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

def get_transform_matrix(p0, p1, p2, p3):
    dx1 = p1[0] - p0[0]
    dy1 = p1[1] - p0[1]
    dz1 = p1[2] - p0[2]

    dx2 = p3[0] - p2[0]
    dy2 = p3[1] - p2[1]
    dz2 = p3[2] - p2[2]

    # theta1 = np.pi/2 if dz1 == 0 else atan(dx1/dz1)
    # theta2 = np.pi/2 if dx1**2 + dz1**2 == 0 else atan(dy1/np.sqrt(dx1**2 + dz1**2))

    # theta3 = np.pi/2 if dx2**2 + dz2**2 == 0 else atan(dy2/np.sqrt(dx2**2 + dz2**2))
    # theta4 = np.pi/2 if dz2 == 0 else atan(dx2/dz2)

    l1 = np.sqrt(dx1**2 + dy1**2 + dz1**2)
    l2 = np.sqrt(dx2**2 + dy2**2 + dz2**2)

    theta1 = acos(dz1/np.sqrt(dx1**2 + dz1**2))
    theta2 = acos(np.sqrt(dx1**2 + dz1**2)/l1)

    theta3 = acos(np.sqrt(dx2**2 + dz2**2)/l2)
    theta4 = acos(dz2/np.sqrt(dx2**2 + dz2**2))


    f = l2/l1

    a1 = translate(-p0[0],-p0[1],-p0[2])
    a2 = yrotate(-theta1)
    a3 = xrotate(theta2)
    a4 = scale(f,f,f)
    a5 = xrotate(-theta3)
    a6 = yrotate(theta4)
    a7 = translate(p2[0],p2[1],p2[2])

    return np.matmul(a7,np.matmul(a6,np.matmul(a5,np.matmul(a4,np.matmul(a3,np.matmul(a2,a1))))))


# noinspection PyTypeChecker
class Hand:
    def __init__(self,scene, points=None):
        self.fingers = None
        self.distances = {}
        self.meshes = {}
        self.nodes = {}

        self.camera = None
        self.scene = scene

        if points:
            self.make_fingers(points)
            self.find_distance_make_mesh_color_node()

        self.add_camera()
        self.add_scene_lighting()
        self.renderer = pyrender.OffscreenRenderer(500, 500)
        self.i = 0

    def add_camera(self):
        cam = pyrender.OrthographicCamera(xmag=1, ymag=1)
        self.camera = pyrender.Node(camera=cam)
        self.scene.add_node(self.camera)
        self.scene.set_pose(self.camera, pose=np.array([[1, 0, 0, 0],
                                                        [0, 1, 0, 0],
                                                        [0, 0, 1, 1],
                                                        [0, 0, 0, 1]]))

    def take_snapshot(self, tag=''):
        color, _ = self.renderer.render(self.scene)
        im = Image.fromarray(color)
        im.save(f"./test/snapshot_{self.i}_{tag}.jpeg")
        print(f"Taking snapshot {self.i}. {tag}")
        self.i += 1

    def make_fingers(self, points):
        self.fingers_old = self.fingers
        self.fingers = {
            'if': '',
            'mf': '',
            'rf': '',
            'pf': '',
        } 
        current = 1
        for i in self.fingers:
            if i != 'wrist':
                fin = {}
                for j in range(4):
                    fin[j] = [points[current]['x'], points[current]['y'], points[current]['z']]
                    current += 1
                self.fingers[i] = fin
        self.fingers['wrist'] = [points[0]['x'], points[0]['y'], points[0]['z']]
        return self.fingers

    

    def find_distance_make_mesh_color_node(self):
        for i in self.fingers:
            if i != 'wrist':
                dis = {}
                mes = {}
                nod = {}
                for j in range(3):
                    dis[j] = distance(self.fingers[i][j], self.fingers[i][j + 1])
                    mes_temp = trimesh.creation.cylinder(dis[j] / 3,
                                                         segment=(self.fingers[i][j], self.fingers[i][j + 1]))
                    mes_temp.vertex_colors = np.random.uniform(size=mes_temp.vertices.shape)
                    mes[j] = pyrender.Mesh.from_trimesh(mes_temp)
                    nod[j] = self.scene.add(mes[j])

                self.distances[i] = dis
                self.meshes[i] = mes
                self.nodes[i] = nod
        self.distances['wrist'] = distance(self.fingers['if'][0], self.fingers['pf'][0])
        self.meshes['wrist'] = trimesh.creation.cylinder(self.distances['wrist'] / 2,
                                                         segment=(self.fingers['wrist'], self.fingers['mf'][0]))
        self.meshes['wrist'].vertex_colors = np.random.uniform(size=self.meshes['wrist'].vertices.shape)
        self.meshes['wrist'] = pyrender.Mesh.from_trimesh(self.meshes['wrist'])  # , smooth=False)
        self.nodes['wrist'] = self.scene.add(self.meshes['wrist'])
        return self.nodes

    def add_scene_lighting(self):
        arr = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 1],
               [0, 0, 0, 1]]

        light = pyrender.SpotLight(color=(255, 255, 255), intensity=12.0,
                                   innerConeAngle=0,
                                   outerConeAngle=np.pi / 2.0)
        self.scene.add(light, pose=arr)

    def delete_hand_nodes(self):
        for i in self.nodes:
            if i != 'wrist':
                for j in range(3):
                    self.scene.remove_node(self.nodes[i][j])
        self.scene.remove_node(self.nodes['wrist'])

    def transform(self):
        if self.fingers_old:
            for i in self.fingers:
                if i != 'wrist':
                    for j in range(3):
                        mat = get_transform_matrix(self.fingers_old[i][j], self.fingers_old[i][j+1], self.fingers[i][j], self.fingers[i][j+1])
                        cur_mat = self.scene.get_pose(self.nodes[i][j])
                        mat_fin = np.dot(cur_mat, mat)
                        self.scene.set_pose(self.nodes[i][j], pose=mat_fin)
            mat = get_transform_matrix(self.fingers_old['wrist'], self.fingers_old['mf'][0], self.fingers['wrist'], self.fingers['mf'][0])
            cur_mat = self.scene.get_pose(self.nodes['wrist'])
            mat_fin = np.dot(cur_mat, mat)
            self.scene.set_pose(self.nodes['wrist'], pose=mat_fin)


hand_coords = [{'x': 0.4151753783226013, 'y': 0.7605129480361938, 'z': 4.250686470186338e-05},
               {'x': 0.4972763657569885, 'y': 0.7331602573394775, 'z': -0.04233528673648834},
               {'x': 0.5666843056678772, 'y': 0.6687094569206238, 'z': -0.07530687004327774},
               {'x': 0.6275107860565186, 'y': 0.6153227090835571, 'z': -0.10305748134851456},
               {'x': 0.6786800026893616, 'y': 0.5903015732765198, 'z': -0.14119328558444977},
               {'x': 0.5138599872589111, 'y': 0.5082778930664062, 'z': -0.06475142389535904},
               {'x': 0.5436963438987732, 'y': 0.39067167043685913, 'z': -0.09653126448392868},
               {'x': 0.5592374801635742, 'y': 0.3177816867828369, 'z': -0.11633691936731339},
               {'x': 0.5722423791885376, 'y': 0.25653913617134094, 'z': -0.13290783762931824},
               {'x': 0.45963528752326965, 'y': 0.48769012093544006, 'z': -0.06724841147661209},
               {'x': 0.4686684310436249, 'y': 0.3511433005332947, 'z': -0.10220623016357422},
               {'x': 0.47671350836753845, 'y': 0.26208817958831787, 'z': -0.12972985208034515},
               {'x': 0.4847656786441803, 'y': 0.19382691383361816, 'z': -0.14857076108455658},
               {'x': 0.40846574306488037, 'y': 0.499553382396698, 'z': -0.07332062721252441},
               {'x': 0.39219510555267334, 'y': 0.3804429769515991, 'z': -0.10998094826936722},
               {'x': 0.387982577085495, 'y': 0.29997676610946655, 'z': -0.14028529822826385},
               {'x': 0.3901064991950989, 'y': 0.23482921719551086, 'z': -0.16343916952610016},
               {'x': 0.3623931109905243, 'y': 0.5395188927650452, 'z': -0.0801873430609703},
               {'x': 0.3187524080276489, 'y': 0.4670122563838959, 'z': -0.11366967111825943},
               {'x': 0.29208528995513916, 'y': 0.41626235842704773, 'z': -0.1377883106470108},
               {'x': 0.27184945344924927, 'y': 0.3654676377773285, 'z': -0.15765070915222168}]
if __name__ == '__main__':
    hand = Hand(hand_coords)
    hand.take_snapshot('test')
    hand.delete_hand_nodes()
    hand.take_snapshot('no hands')
