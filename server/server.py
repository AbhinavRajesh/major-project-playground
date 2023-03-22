import os, asyncio, websockets
from _thread import *
import json

# create handler for each connection
global connected_clients, client_positions
connected_clients = []
client_positions = {}
seek = 0


def get_file_path(filename="", local=True):
    if local:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(os.path.join(BASE_DIR, "test"), filename)
    else:
        return filename


async def logger(current_client):
    message = await current_client.recv()
    print(f"[LOGGER]:", message)


async def send_position():
    global connected_clients
    while True:
        await asyncio.sleep(5)
        for client in connected_clients:
            data = {
                "client": str(client.id),
                "positions": list(client_positions.values()),
                "type": "coordinates",
            }
            print(f"Sending {data=}")
            await client.send(json.dumps(data))

async def handler(current_client, path):
    global connected_clients, seek
    connected_clients.append(current_client)
    print(current_client.id, "joined.")
    print(f"Now total {len(connected_clients)} clients")
    await current_client.send(json.dumps({"seek": seek}))
    asyncio.get_event_loop().create_task(send_position())
    while True:
        data = await current_client.recv()
        data = json.loads(data)
        if "type" in list(data.keys()):
            if data["type"] == "coordinates":
                position = json.dumps(data["position"])
                print(position)
                direction = data["direction"]
                for client in connected_clients:
                    data = {
                        "client": str(client.id),
                        "position": position,
                        "direction": direction,
                        "type": "coordinates",
                    }
                    client_positions[str(client.id)] = list(position.values())
            elif data["type"] == "seek":
                if connected_clients.index(current_client) == 0:
                    data = await current_client.recv()
                    data = json.loads(data)
                    seek = data["seek"]


def main():
    Websocket_Server = websockets.serve(handler, "127.0.0.1", 8080)

    try:
        asyncio.get_event_loop().run_until_complete(Websocket_Server)
        asyncio.get_event_loop().run_forever()
    except Exception as e:
        print("server crashed", e)


if __name__ == "__main__":
    main()
