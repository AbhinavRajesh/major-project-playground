import os, asyncio, websockets, ffmpeg_streaming
from ffmpeg_streaming import Formats
from _thread import start_new_thread


def get_file_path(filename="", local=True):
    if local:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(os.path.join(BASE_DIR, "test"), filename)
    else:
        return filename


global connected_clients, input_path, output_path
input_path = get_file_path("sample_video.mp4")
output_path = os.path.join(get_file_path("output"), "dash.mpd")
connected_clients = []


async def Stream_Video():
    video = ffmpeg_streaming.input(input_path)
    dash = video.dash(Formats.h264())
    dash.auto_generate_representations()
    dash.output(output_path)
    dash.output(output_path, async_run=False)


async def handle_websocket(current_client, path):
    # This function is called every time a client connects to the server
    print("Client connected")
    global connected_clients
    connected_clients.append(current_client)

    try:
        with open(output_path, "r") as f:
            data = f.read()
            await current_client.send(data)

    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected")
        connected_clients.remove(current_client)
    except Exception as e:
        print("Some error occured", e)

    # break


async def main():
    # Run the WebSocket server and the other function concurrently using asyncio.gather()
    async with websockets.serve(handle_websocket, "127.0.0.1", 8080):
        print("WebSocket server started")
        await asyncio.gather(Stream_Video())


asyncio.run(main())
