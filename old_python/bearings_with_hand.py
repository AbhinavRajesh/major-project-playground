from hand import Hand, hand_coords
import pyrender
import trimesh
import numpy as np
from PIL import Image

hand = Hand(hand_coords)

hand.scene.set_pose(hand.camera, np.array([[-1, 0, 0, 0],
                                           [0, 1, 0, 0],
                                           [0, 0, -1, -1],
                                           [0, 0, 0, 1]]))
translation_matrix = np.array([[1, 0, 0, 0.1],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
for _ in range(10):
    for node in hand.scene.nodes:
        if node != hand.camera:
            pose = np.matmul(node.matrix, translation_matrix)
            hand.scene.set_pose(node, pose=pose)
    hand.take_snapshot()

translation_matrix = np.array([[1, 0, 0, -0.1],
                               [0, 1, 0, -0.1],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
for _ in range(10):
    for node in hand.scene.nodes:
        if node != hand.camera:
            pose = np.matmul(node.matrix, translation_matrix)
            hand.scene.set_pose(node, pose=pose)
    hand.take_snapshot()

translation_matrix = np.array([[1, 0, 0, 0],
                               [0, 1, 0, 0.1],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
for _ in range(10):
    for node in hand.scene.nodes:
        if node != hand.camera:
            pose = np.matmul(node.matrix, translation_matrix)
            hand.scene.set_pose(node, pose=pose)
    hand.take_snapshot()
