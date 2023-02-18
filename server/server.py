import os, asyncio, websockets, cv2, subprocess, time
from _thread import *
import ssl

# create handler for each connection
global connected_clients
connected_clients = []


def get_file_path(filename="", local=True):
    if local:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(os.path.join(BASE_DIR, "test"), filename)
    else:
        return filename


FFMPEG_PARAMS = [
    "-i",
    get_file_path("sample_video.mp4"),
    "-c:v",
    "copy",
    "-c:a",
    "copy",
    "-hls_time",
    "10",
    "-hls_list_size",
    "0",
    "-f",
    "hls",
    "pipe:1",
]


async def logger(current_client):
    message = await current_client.recv()
    print(f"[LOGGER]:", message)


async def handler(current_client, path):
    print(f"new client {current_client.id}")
    ffmpeg_process = subprocess.Popen(
        ["ffmpeg", *FFMPEG_PARAMS], stdout=subprocess.PIPE
    )
    if path == "/logger":
        logger(current_client)
        return
    global connected_clients
    connected_clients.append(current_client)
    cap = cv2.VideoCapture(get_file_path("sample_video.mp4"))
    i = 1

    while True:
        try:
            # 1000/15 ~= 60 FPS
            # cv2.waitKey(15)
            # ret, frame = cap.read()
            # if not ret:
            #     break
            # data = cv2.imencode(".jpg", frame)[1].tostring()
            data = ffmpeg_process.stdout.read(1024)
            for client in connected_clients:
                try:
                    await client.send(data)
                    print(f"{i} => sending success for client {client.id}")
                except:
                    print(f"{i} => sending failed for client {client.id}")
            time.sleep(0.1)
        except Exception as e:
            print("failed:", i, " =>", e)
        finally:
            i += 1


def main():
    Websocket_Server = websockets.serve(handler, "127.0.0.1", 8080)

    try:
        asyncio.get_event_loop().run_until_complete(Websocket_Server)
        asyncio.get_event_loop().run_forever()
    except Exception as e:
        print("server crashed", e)


if __name__ == "__main__":
    main()
# para thara what is the current problem?
# Video client n receive avanilla
# Tried solution according to  chatgpt3
# Next solution? search!!!! oh no developer slep off.""
