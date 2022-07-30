from flask import Flask, render_template
from flask_socketio import SocketIO, emit
# import re
from PIL import Image
import cv2
import base64
import numpy as np
import io
# import cv2
from flask import request
# import logging
import time
import os
os.environ['PYOPENGL_PLATFORM'] = 'egl'

import trimesh
import pyrender
from math import sin, cos
from hand1 import Hand

import mediapipe as mp
import multiprocessing as multip



# from shared_ndarray import SharedNDArray
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

from functools import wraps
import errno
import os
import signal

processdict = {}
memorydict = {}
outputdict = {}
counter = {}
retries = {}
hand=None
# hands =  mp_hands.Hands(
#         min_detection_confidence=0.5,
#         min_tracking_confidence=0.5)

def distance(p1,p2):
   return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)


class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):

            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, 2, 2)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

def process(md,op):

    @timeout(1)
    def timout_analyze_hand(image):
        image.flags.writeable = False
        results = hands.process(image)
        return results
    
    hands =  mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)
    
    count =0
    scene = pyrender.Scene(bg_color=(255,255,255,0))
    camera = pyrender.OrthographicCamera(xmag=.35 , ymag=.35)
    nc = pyrender.Node(camera=camera)
    scene.add_node(nc)

    arr = [[1,0,0,.5],
        [0,-1,0,.5],
        [0,0,-1,-1],
        [0,0,0,1]]
        
    # scene.add(camera, pose=camera_pose)
    light = pyrender.SpotLight(color=(255,255,255), intensity=6,
                            innerConeAngle=0,
                            outerConeAngle=np.pi/2.0,range=10)
    scene.add(light, pose=arr)
    scene.set_pose(nc, pose=np.array(arr))
    r = pyrender.OffscreenRenderer(320, 240)
    hand = None
    while True:
        if not md.empty():
            mda = md.get()
            if mda['type']=='img':
                mdarray = np.copy(mda['data'])
                results = timout_analyze_hand(mdarray)
                image = mdarray
                # print(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks:
                    # print(results.multi_hand_landmarks[0].landmark)

                    for hand_landmarks in results.multi_hand_landmarks:
                        # print(hand_landmarks.landmark[0].x)
                        mp_drawing.draw_landmarks(
                            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                        break
                    if not hand:
                        hand = Hand(scene,points=results.multi_hand_landmarks[0].landmark,mode=True)
                    else:
                        hand.make_fingers(points=results.multi_hand_landmarks[0].landmark,mode=True)
                        hand.transform()  

                    rest,depth = r.render(scene, flags=2048)
                    op.put(rest)
            else:
                if not hand:
                    hand = Hand(scene,points=mda['data'])
                else:
                    hand.make_fingers(points=mda['data'])
                    hand.transform()
                rest,depth = r.render(scene, flags=2048)
                op.put(rest)
        # print('hello')
            
        time.sleep(.008)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.event
def send_hand_points(message):

    if  memorydict[request.sid].empty():
        memorydict[request.sid].put({'data':message[-1],'type':'data'})
    counter[request.sid]+=1
    while not outputdict[request.sid].empty():
        results = outputdict[request.sid].get()
        retval, buffer = cv2.imencode('.png', results)
        emit("imgbackend",{"data" : buffer.tobytes()})
       
    

@socketio.event
def my_event(message):

    emit('my_event', {'data': 'got it!'})

@socketio.event
def my_ping():
    emit('my_pong', {'data': ''})

@socketio.event
def connect():

    memorydict[request.sid] = multip.Queue()
    memorydict[request.sid].put({'data':np.zeros((240,320,3),dtype=np.uint8),'type':'img'})
    outputdict[request.sid] = multip.Queue()
    outputdict[request.sid].put(np.zeros((240,320,3),dtype=np.uint8))
    processdict[request.sid] = multip.Process(target=process, daemon=True, kwargs={
        "md": memorydict[request.sid], 'op':outputdict[request.sid]
    })
    counter[request.sid] = 0
    retries[request.sid] = 0
    processdict[request.sid].start()
    print("I'm connected!")

@socketio.event
def disconnect():
    processdict[request.sid].terminate()
    # outputdict[request.sid].close()
    # memorydict[request.sid].close()
    print("I'm disconnected!")

@socketio.event
def image_recv(message):
    global hands
    img = Image.open(io.BytesIO(message))
    counter[request.sid] += 1
    if counter[request.sid] > 600:
        if retries[request.sid] < 5:
            emit("switch","true")
            retries[request.sid] += 1
        counter[request.sid] = 0
    image= np.array(img)
    # print(request.sid)
    if  memorydict[request.sid].empty():
        memorydict[request.sid].put({'data':image,'type':'img'})

    # print(memorydict[request.sid].array)
    
    # processdict[request.sid].join()
    # print(outputdict[request.sid].array)
    # try:
        
    # if results:
    
    while not outputdict[request.sid].empty():
        results = outputdict[request.sid].get(block=False)
        retval, buffer = cv2.imencode('.png', results)
        emit("imgbackend",{"data" : buffer.tobytes()})

        

    # except Exception as e:
    #     print(e)



if __name__ == '__main__':
    # scene = pyrender.Scene()
    # camera = pyrender.OrthographicCamera(xmag=.5 , ymag=.5)
    # nc = pyrender.Node(camera=camera)
    # scene.add_node(nc)

    # arr = [[1,0,0,.5],
    #     [0,-1,0,.5],
    #     [0,0,-1,-1],
    #     [0,0,0,1]]
    # # scene.add(camera, pose=camera_pose)
    # light = pyrender.SpotLight(color=(255,255,255), intensity=12.0,
    #                         innerConeAngle=0,
    #                         outerConeAngle=np.pi/2.0)
    # scene.add(light, pose=arr)
    # scene.set_pose(nc, pose=np.array(arr))
    # r = pyrender.OffscreenRenderer(320, 240)

    socketio.run(app, host='0.0.0.0', port=5000)