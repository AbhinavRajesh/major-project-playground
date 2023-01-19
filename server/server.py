import asyncio, json, websockets

# create handler for each connection
connected_clients = []
messages = []


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
