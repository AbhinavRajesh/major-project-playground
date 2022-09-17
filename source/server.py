import asyncio
import json

import websockets

# create handler for each connection
connected_clients = []
messages = []


async def handler(current_client, path):
    connected_clients.append(current_client)
    while True:
        data = await current_client.recv()
        current_msg = {
            "id": str(current_client.id),
            "cid": connected_clients.index(current_client),
            "msg": data,
        }
        messages.append(current_msg)
        for client in connected_clients:
            await client.send(json.dumps({"messages": messages}))


start_server = websockets.serve(handler, "127.0.0.1", 8080)


asyncio.get_event_loop().run_until_complete(start_server)

try:
    asyncio.get_event_loop().run_forever()
except:
    print("server crashed")
