import os, asyncio, websockets, cv2
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


async def logger(current_client):
    message = await current_client.recv()
    print(f"[LOGGER]:", message)

async def handler(current_client, path):
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
            cv2.waitKey(15)
            ret, frame = cap.read()
            if not ret:
                break
            data = cv2.imencode(".jpg", frame)[1].tostring()
            for client in connected_clients:
                await client.send(data)
            print("success:", i)
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
