import asyncio, json, websockets, base64, time

# create handler for each connection
connected_clients = []


async def handler(current_client, path):
    connected_clients.append(current_client)
    while True:
        data = await current_client.recv()
        data = json.loads(data)
        text_data = data.get("text_data", None)
        timestamp = data.get("timestamp", None)
        # audio_file = open("sample_audio.mp3", "rb").read()
        # audio_data = str(base64.b64encode(audio_file).decode("utf-8"))
        # video_data = data.get("video_data", None)
        # audio_data = data.get("audio_data", None)
        current_msg = {
            "cid": str(current_client.id),
            "cname": connected_clients.index(current_client),
            "text_data": text_data,
            "timestamp": timestamp,
            "audio_data": "",
        }
        for client in connected_clients:
            await client.send(json.dumps(current_msg))


def main():
    Websocket_Server = websockets.serve(handler, "127.0.0.1", 8080)
    asyncio.get_event_loop().run_until_complete(Websocket_Server)
    try:
        asyncio.get_event_loop().run_forever()
    except:
        print("server crashed")


if __name__ == "__main__":
    main()
