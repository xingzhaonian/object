import asyncio
import websockets

async def server(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"收到客户端发来的消息: {message}")

start_server = websockets.serve(server, "127.0.0.1", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print('服务器启动完成>>>')
asyncio.get_event_loop().run_forever()

