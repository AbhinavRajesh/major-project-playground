import numpy as np
import trimesh
import pyrender
import matplotlib.pyplot as plt
from PIL import Image
import time
from math import sin, cos, acos

fuze_trimesh = trimesh.load('examples/models/fuze.obj')
# mesh = pyrender.Mesh.from_trimesh(fuze_trimesh)
# nm = pyrender.Node(mesh=mesh, matrix=np.eye(4))
scene = pyrender.Scene()
# scene.add_node(nm)
camera = pyrender.OrthographicCamera(xmag=1, ymag=1)

s = np.sqrt(2) / 2
points = [{'x': 0.4151753783226013, 'y': 0.7605129480361938, 'z': 4.250686470186338e-05},
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

# points = [{'x': 0.2840995490550995, 'y': 0.8006919622421265, 'z': -5.797784251626581e-05}, {'x': 0.3967483639717102, 'y': 0.8083330392837524, 'z': -0.10079620778560638}, {'x': 0.4994491636753082, 'y': 0.7562743425369263, 'z': -0.1537921279668808}, {'x': 0.5576449632644653, 'y': 0.6757597327232361, 'z': -0.20879708230495453}, {'x': 0.568961501121521, 'y': 0.5798292756080627, 'z': -0.2570129930973053}, {'x': 0.46275120973587036, 'y': 0.479120671749115, 'z': 0.007984028197824955}, {'x': 0.49949026107788086, 'y': 0.3694103956222534, 'z': -0.033009886741638184}, {'x': 0.5181124210357666, 'y': 0.3153204023838043, 'z': -0.08423929661512375}, {'x': 0.5290261507034302, 'y': 0.2990952134132385, 'z': -0.11645250767469406}, {'x': 0.3856457471847534, 'y': 0.43440401554107666, 'z': 0.02365766279399395}, {'x': 0.4016180634498596, 'y': 0.30536913871765137, 'z': 0.02452361211180687}, {'x': 0.4063650071620941, 'y': 0.22299987077713013, 'z': 0.00018103697220794857}, {'x': 0.41145598888397217, 'y': 0.18187585473060608, 'z': -0.016167225316166878}, {'x': 0.31327521800994873, 'y': 0.43463513255119324, 'z': 0.017907777801156044}, {'x': 0.31743723154067993, 'y': 0.31184715032577515, 'z': 0.005905756726861}, {'x': 0.31112587451934814, 'y': 0.23722457885742188, 'z': -0.02658456563949585}, {'x': 0.3065807819366455, 'y': 0.195704847574234, 'z': -0.04752315580844879}, {'x': 0.2376718670129776, 'y': 0.4655369520187378, 'z': -0.0028597889468073845}, {'x': 0.22319740056991577, 'y': 0.37526750564575195, 'z': -0.02982320450246334}, {'x': 0.2117592692375183, 'y': 0.33128541707992554, 'z': -0.06110120192170143}, {'x': 0.20671701431274414, 'y': 0.30615681409835815, 'z': -0.0798749253153801}]

camera_pose = np.array([
    [0.0, -s, s, 0.3],
    [1.0, 0.0, 0.0, 0.0],
    [0.0, s, s, 0.35],
    [0.0, 0.0, 0.0, 1.0],
])

nc = pyrender.Node(camera=camera)


def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


# index finger
if_tip = [points[8]['x'], points[8]['y'], points[8]['z']]
if_dip = [points[7]['x'], points[7]['y'], points[7]['z']]
if_pip = [points[6]['x'], points[6]['y'], points[6]['z']]
if_mcp = [points[5]['x'], points[5]['y'], points[5]['z']]

# middle finger
mf_tip = [points[12]['x'], points[12]['y'], points[12]['z']]
mf_dip = [points[11]['x'], points[11]['y'], points[11]['z']]
mf_pip = [points[10]['x'], points[10]['y'], points[10]['z']]
mf_mcp = [points[9]['x'], points[9]['y'], points[9]['z']]

# ring finger
rf_tip = [points[16]['x'], points[16]['y'], points[16]['z']]
rf_dip = [points[15]['x'], points[15]['y'], points[15]['z']]
rf_pip = [points[14]['x'], points[14]['y'], points[14]['z']]
rf_mcp = [points[13]['x'], points[13]['y'], points[13]['z']]

# pinky finger
pf_tip = [points[20]['x'], points[20]['y'], points[20]['z']]
pf_dip = [points[19]['x'], points[19]['y'], points[19]['z']]
pf_pip = [points[18]['x'], points[18]['y'], points[18]['z']]
pf_mcp = [points[17]['x'], points[17]['y'], points[17]['z']]

# thumb finger
tf_tip = [points[4]['x'], points[4]['y'], points[4]['z']]
tf_dip = [points[3]['x'], points[3]['y'], points[3]['z']]
tf_pip = [points[2]['x'], points[2]['y'], points[2]['z']]
tf_mcp = [points[1]['x'], points[1]['y'], points[1]['z']]

# wrist
wrist = [points[0]['x'], points[0]['y'], points[0]['z']]

if_dis_1 = distance(if_tip, if_dip)
if_dis_2 = distance(if_dip, if_pip)
if_dis_3 = distance(if_pip, if_mcp)

mf_dis_1 = distance(mf_tip, mf_dip)
mf_dis_2 = distance(mf_dip, mf_pip)
mf_dis_3 = distance(mf_pip, mf_mcp)

rf_dis_1 = distance(rf_tip, rf_dip)
rf_dis_2 = distance(rf_dip, rf_pip)
rf_dis_3 = distance(rf_pip, rf_mcp)

pf_dis_1 = distance(pf_tip, pf_dip)
pf_dis_2 = distance(pf_dip, pf_pip)
pf_dis_3 = distance(pf_pip, pf_mcp)

tf_dis_1 = distance(tf_tip, tf_dip)
tf_dis_2 = distance(tf_dip, tf_pip)
tf_dis_3 = distance(tf_pip, tf_mcp)

wrist_dis = distance(if_mcp, pf_mcp)

if_cy_1 = trimesh.creation.cylinder(if_dis_1 / 3, segment=(if_tip, if_dip))
if_cy_2 = trimesh.creation.cylinder(if_dis_2 / 3, segment=(if_dip, if_pip))
if_cy_3 = trimesh.creation.cylinder(if_dis_3 / 3, segment=(if_pip, if_mcp))

mf_cy_1 = trimesh.creation.cylinder(mf_dis_1 / 3, segment=(mf_tip, mf_dip))
mf_cy_2 = trimesh.creation.cylinder(mf_dis_2 / 3, segment=(mf_dip, mf_pip))
mf_cy_3 = trimesh.creation.cylinder(mf_dis_3 / 3, segment=(mf_pip, mf_mcp))

rf_cy_1 = trimesh.creation.cylinder(rf_dis_1 / 3, segment=(rf_tip, rf_dip))
rf_cy_2 = trimesh.creation.cylinder(rf_dis_2 / 3, segment=(rf_dip, rf_pip))
rf_cy_3 = trimesh.creation.cylinder(rf_dis_3 / 3, segment=(rf_pip, rf_mcp))

pf_cy_1 = trimesh.creation.cylinder(pf_dis_1 / 3, segment=(pf_tip, pf_dip))
pf_cy_2 = trimesh.creation.cylinder(pf_dis_2 / 3, segment=(pf_dip, pf_pip))
pf_cy_3 = trimesh.creation.cylinder(pf_dis_3 / 3, segment=(pf_pip, pf_mcp))

tf_cy_1 = trimesh.creation.cylinder(tf_dis_1 / 3, segment=(tf_tip, tf_dip))
tf_cy_2 = trimesh.creation.cylinder(tf_dis_2 / 3, segment=(tf_dip, tf_pip))
tf_cy_3 = trimesh.creation.cylinder(tf_dis_3 / 3, segment=(tf_pip, tf_mcp))

wrist_sp = trimesh.creation.cylinder(wrist_dis / 2, segment=(wrist, mf_mcp))

if_cy_1.visual.vertex_colors = np.random.uniform(size=if_cy_1.vertices.shape)
if_cy_2.visual.vertex_colors = np.random.uniform(size=if_cy_2.vertices.shape)
if_cy_3.visual.vertex_colors = np.random.uniform(size=if_cy_3.vertices.shape)

mf_cy_1.visual.vertex_colors = np.random.uniform(size=mf_cy_1.vertices.shape)
mf_cy_2.visual.vertex_colors = np.random.uniform(size=mf_cy_2.vertices.shape)
mf_cy_3.visual.vertex_colors = np.random.uniform(size=mf_cy_3.vertices.shape)

rf_cy_1.visual.vertex_colors = np.random.uniform(size=rf_cy_1.vertices.shape)
rf_cy_2.visual.vertex_colors = np.random.uniform(size=rf_cy_2.vertices.shape)
rf_cy_3.visual.vertex_colors = np.random.uniform(size=rf_cy_3.vertices.shape)

pf_cy_1.visual.vertex_colors = np.random.uniform(size=pf_cy_1.vertices.shape)
pf_cy_2.visual.vertex_colors = np.random.uniform(size=pf_cy_2.vertices.shape)
pf_cy_3.visual.vertex_colors = np.random.uniform(size=pf_cy_3.vertices.shape)

tf_cy_1.visual.vertex_colors = np.random.uniform(size=tf_cy_1.vertices.shape)
tf_cy_2.visual.vertex_colors = np.random.uniform(size=tf_cy_2.vertices.shape)
tf_cy_3.visual.vertex_colors = np.random.uniform(size=tf_cy_3.vertices.shape)

print(tf_cy_3.vertices.shape)
wrist_sp.visual.vertex_colors = np.random.uniform(size=wrist_sp.vertices.shape)

if_m_1 = pyrender.Mesh.from_trimesh(if_cy_1, smooth=False)
if_m_2 = pyrender.Mesh.from_trimesh(if_cy_2, smooth=False)
if_m_3 = pyrender.Mesh.from_trimesh(if_cy_3, smooth=False)

mf_m_1 = pyrender.Mesh.from_trimesh(mf_cy_1, smooth=False)
mf_m_2 = pyrender.Mesh.from_trimesh(mf_cy_2, smooth=False)
mf_m_3 = pyrender.Mesh.from_trimesh(mf_cy_3, smooth=False)

rf_m_1 = pyrender.Mesh.from_trimesh(rf_cy_1, smooth=False)
rf_m_2 = pyrender.Mesh.from_trimesh(rf_cy_2, smooth=False)
rf_m_3 = pyrender.Mesh.from_trimesh(rf_cy_3, smooth=False)

pf_m_1 = pyrender.Mesh.from_trimesh(pf_cy_1, smooth=False)
pf_m_2 = pyrender.Mesh.from_trimesh(pf_cy_2, smooth=False)
pf_m_3 = pyrender.Mesh.from_trimesh(pf_cy_3, smooth=False)

tf_m_1 = pyrender.Mesh.from_trimesh(tf_cy_1, smooth=False)
tf_m_2 = pyrender.Mesh.from_trimesh(tf_cy_2, smooth=False)
tf_m_3 = pyrender.Mesh.from_trimesh(tf_cy_3, smooth=False)

wrist_m = pyrender.Mesh.from_trimesh(wrist_sp, smooth=False)

# if_nm_1 = pyrender.Node(mesh=if_m_1, matrix=np.eye(4))
# nm2 = pyrender.Node(mesh=m2, matrix=np.eye(4))
scene.add(wrist_m)

if_nc = scene.add(if_m_1)
scene.add(if_m_2)
scene.add(if_m_3)

scene.add(mf_m_1)
scene.add(mf_m_2)
scene.add(mf_m_3)

scene.add(rf_m_1)
scene.add(rf_m_2)
scene.add(rf_m_3)

scene.add(pf_m_1)
scene.add(pf_m_2)
scene.add(pf_m_3)

scene.add(tf_m_1)
scene.add(tf_m_2)
scene.add(tf_m_3)

scene.add_node(nc)


def getangles(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    c = p1[2] - p2[2]

    l = np.sqrt(a * a + b * b + c * c)

    x = acos(a / l)
    y = acos(b / l)
    z = acos(c / l)

    return x, y, z


def eulerrot(x, y, z):
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


def scalemat(p3, p4):
    sx = (p3[0] - p4[0])
    sy = (p3[1] - p4[1])
    sz = (p3[2] - p4[2])

    x = p3[0]
    y = p3[1]
    z = p3[2]

    return np.array([[sx, sy, sz, x],
                     [sx, sy, sz, y],
                     [sx, sy, sz, z],
                     [0, 0, 0, 1]])


points = [{'x': 0.2840995490550995, 'y': 0.8006919622421265, 'z': -5.797784251626581e-05},
          {'x': 0.3967483639717102, 'y': 0.8083330392837524, 'z': -0.10079620778560638},
          {'x': 0.4994491636753082, 'y': 0.7562743425369263, 'z': -0.1537921279668808},
          {'x': 0.5576449632644653, 'y': 0.6757597327232361, 'z': -0.20879708230495453},
          {'x': 0.568961501121521, 'y': 0.5798292756080627, 'z': -0.2570129930973053},
          {'x': 0.46275120973587036, 'y': 0.479120671749115, 'z': 0.007984028197824955},
          {'x': 0.49949026107788086, 'y': 0.3694103956222534, 'z': -0.033009886741638184},
          {'x': 0.5181124210357666, 'y': 0.3153204023838043, 'z': -0.08423929661512375},
          {'x': 0.5290261507034302, 'y': 0.2990952134132385, 'z': -0.11645250767469406},
          {'x': 0.3856457471847534, 'y': 0.43440401554107666, 'z': 0.02365766279399395},
          {'x': 0.4016180634498596, 'y': 0.30536913871765137, 'z': 0.02452361211180687},
          {'x': 0.4063650071620941, 'y': 0.22299987077713013, 'z': 0.00018103697220794857},
          {'x': 0.41145598888397217, 'y': 0.18187585473060608, 'z': -0.016167225316166878},
          {'x': 0.31327521800994873, 'y': 0.43463513255119324, 'z': 0.017907777801156044},
          {'x': 0.31743723154067993, 'y': 0.31184715032577515, 'z': 0.005905756726861},
          {'x': 0.31112587451934814, 'y': 0.23722457885742188, 'z': -0.02658456563949585},
          {'x': 0.3065807819366455, 'y': 0.195704847574234, 'z': -0.04752315580844879},
          {'x': 0.2376718670129776, 'y': 0.4655369520187378, 'z': -0.0028597889468073845},
          {'x': 0.22319740056991577, 'y': 0.37526750564575195, 'z': -0.02982320450246334},
          {'x': 0.2117592692375183, 'y': 0.33128541707992554, 'z': -0.06110120192170143},
          {'x': 0.20671701431274414, 'y': 0.30615681409835815, 'z': -0.0798749253153801}]

# index finger
if_tip = [points[8]['x'], points[8]['y'], points[8]['z']]
if_dip = [points[7]['x'], points[7]['y'], points[7]['z']]
if_pip = [points[6]['x'], points[6]['y'], points[6]['z']]
if_mcp = [points[5]['x'], points[5]['y'], points[5]['z']]

# middle finger
mf_tip = [points[12]['x'], points[12]['y'], points[12]['z']]
mf_dip = [points[11]['x'], points[11]['y'], points[11]['z']]
mf_pip = [points[10]['x'], points[10]['y'], points[10]['z']]
mf_mcp = [points[9]['x'], points[9]['y'], points[9]['z']]

# ring finger
rf_tip = [points[16]['x'], points[16]['y'], points[16]['z']]
rf_dip = [points[15]['x'], points[15]['y'], points[15]['z']]
rf_pip = [points[14]['x'], points[14]['y'], points[14]['z']]
rf_mcp = [points[13]['x'], points[13]['y'], points[13]['z']]

# pinky finger
pf_tip = [points[20]['x'], points[20]['y'], points[20]['z']]
pf_dip = [points[19]['x'], points[19]['y'], points[19]['z']]
pf_pip = [points[18]['x'], points[18]['y'], points[18]['z']]
pf_mcp = [points[17]['x'], points[17]['y'], points[17]['z']]

# thumb finger
tf_tip = [points[4]['x'], points[4]['y'], points[4]['z']]
tf_dip = [points[3]['x'], points[3]['y'], points[3]['z']]
tf_pip = [points[2]['x'], points[2]['y'], points[2]['z']]
tf_mcp = [points[1]['x'], points[1]['y'], points[1]['z']]

# wrist
wrist = [points[0]['x'], points[0]['y'], points[0]['z']]

x, y, z = getangles(if_tip, if_dip)
rotmat = eulerrot(x, y, z)
scalemat = scalemat(if_tip, if_dip)

transmat = np.multiply(rotmat, scalemat)

arr = [[-1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, -1, -1],
       [0, 0, 0, 1]]
# scene.add(camera, pose=camera_pose)
light = pyrender.SpotLight(color=(255, 255, 255), intensity=12.0,
                           innerConeAngle=0,
                           outerConeAngle=np.pi / 2.0)
scene.add(light, pose=arr)
scene.set_pose(nc, pose=np.array(arr))
r = pyrender.OffscreenRenderer(500, 500)

i = 3
color, depth = r.render(scene)
im = Image.fromarray(color)
im.save(f"./test/your_file_{i}.jpeg")

i = 2
scene.set_pose(if_nc, pose=np.array(scalemat))
color, depth = r.render(scene)
im = Image.fromarray(color)
im.save(f"./test/your_file_{i}.jpeg")


class hand:
    def __init__(self, points=None):
        self.fingers = {
            'if': '',
            'mf': '',
            'rf': '',
            'pf': '',
        }
        self.distances = {}
        self.meshes = {}
        self.nodes = {}
        if points:
            self.make_fingers(points)
            self.find_distance_make_mesh_color()

    def make_fingers(self, points):
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
                    nod[j] = scene.add(mes[j])

                self.distances[i] = dis
                self.meshes[i] = mes
                self.nodes[i] = nod
        self.distances['wrist'] = distance(self.fingers['if'][0], self.fingers['pf'][0])
        self.meshes['wrist'] = trimesh.creation.cylinder(self.distances['wrist'] / 2,
                                                         segment=(self.fingers['wrist'], self.fingers['mf'][0]))
        self.meshes['wrist'].vertex_colors = np.random.uniform(size=self.meshes['wrist'].vertices.shape)
        self.meshes['wrist'] = pyrender.Mesh.from_trimesh(self.meshes['wrist'])  # , smooth=False)
        self.nodes['wrist'] = scene.add(self.meshes['wrist'])
        return self.nodes

    def delete_nodes(self):
        for i in self.nodes:
            if i != 'wrist':
                for j in range(3):
                    scene.remove_node(self.nodes[i][j])
        scene.remove_node(self.nodes['wrist'])

    def transform(self,p1,p2,p3,p4):
        orgmat = np.array([[1, 0, 0, -p1[0]],
                  [0, 1, 0, -p1[1]],
                  [0, 0, 1, -p1[2]],
                  [0, 0, 0, 1]])

        a = p2[0] - p1[0]
        b = p2[1] - p1[1]
        c = p2[2] - p1[2]

        scamat = np.array([[1/np.abs(a), 0, 0, 0],
                  [0, 1/np.abs(b), 0, 0],
                  [0, 0, 1/np.abs(c), 0],
                  [0, 0, 0, 1]])

        x,y,z = getangles(p1,p2)
        

        



      
