import cv2
import socket
import time
import struct
import pickle

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

# Open the video file using OpenCV
video_capture = cv2.VideoCapture("dummy.webm")

# Set the frame rate for the video
frame_rate = 60

# Create a socket for sending data to clients
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout for the socket
sock.settimeout(1.0 / frame_rate)

# Set the address and port for the socket
server_address = ('127.0.0.1', 5050)

# Initialize a counter for the frame number
frame_number = 0

# Initi the time
second = 0 + 1/frame_rate

video_capture.set(cv2.CAP_PROP_POS_MSEC, second*1000)

# Read the first frame from the video
success, frame = video_capture.read()

# Loop until the video is finished or the user breaks the loop
while success:
    # Increment the frame number
    frame_number += 1

    # Encode the frame as a JPEG image and send it to the clients
    jpeg_frame = cv2.imencode('.jpg', frame, encode_param)[1]
    data = pickle.dumps(jpeg_frame, 0)
    size = len(data)
    print(size)
    sock.sendto("hello".encode(), server_address)

    # Sleep for the desired amount of time before sending the next frame
    time.sleep(1.0 / frame_rate)

    # Change the time
    second += 1/frame_rate

    video_capture.set(cv2.CAP_PROP_POS_MSEC, second*1000)

    # Read the next frame from the video
    success, frame = video_capture.read()

# Close the video capture and socket
video_capture.release()
sock.close()
