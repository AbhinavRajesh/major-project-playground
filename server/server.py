import os, asyncio, json, websockets, ffmpeg_streaming
from ffmpeg_streaming import Formats

# create handler for each connection
connected_clients = []
messages = []


def get_file_path(filename="", local=True):
    if local:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(os.path.join(BASE_DIR, "test"), filename)
    else:
        return filename


async def streamer():
    video_stream = ffmpeg_streaming.input(get_file_path("sample_video.mp4"))
    video_dash = video_stream.dash(Formats.h264())
    video_dash.auto_generate_representations()
    video_dash.output(get_file_path("sample_video.mpd"))
    current_msg = {
        "video_data": "video_data",
    }
    for client in connected_clients:
        await client.send(json.dumps(current_msg))


async def handler(current_client, path):
    connected_clients.append(current_client)
    while True:
        data = await current_client.recv()
        data = json.loads(data)
        text_data = data.get("text_data", None)
        timestamp = data.get("timestamp", None)
        audio_data = ""
        video_data = ""
        # video_data = data.get("video_data", None)
        # audio_data = data.get("audio_data", None)
        current_msg = {
            "cid": str(current_client.id),
            "cname": connected_clients.index(current_client) + 1,
            "timestamp": timestamp,
            "text_data": text_data,
            "audio_data": audio_data,
            "video_data": video_data,
        }
        messages.append(current_msg)
        for client in connected_clients:
            await client.send(json.dumps({"messages": messages}))


def main():
    Websocket_Server = websockets.serve(handler, "127.0.0.1", 8080)
    asyncio.get_event_loop().run_until_complete(Websocket_Server)
    try:
        asyncio.get_event_loop().run_forever()
    except:
        print("server crashed")


if __name__ == "__main__":
    main()
