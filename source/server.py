import asyncio
import json

import websockets

# create handler for each connection
connected_clients = []
messages = []


async def handler(websocket, path):
    connected_clients.append(websocket.id)
    while True:
        data = await websocket.recv()
        current_msg = {
            "id": str(websocket.id),
            "cid": connected_clients.index(websocket.id),
            "msg": data,
        }
        messages.append(current_msg)
        await websocket.send(json.dumps({"messages": messages}))


start_server = websockets.serve(handler, "127.0.0.1", 8080)


asyncio.get_event_loop().run_until_complete(start_server)

try:
    asyncio.get_event_loop().run_forever()
except:
    print("server crashed")
