import asyncio
import websockets

async def client():
    async with websockets.connect("ws://127.0.0.1:8765") as websocket:
        while True:
            message = input('请输入要发送的消息>>>')
            if message == 'exit':
                break
            await websocket.send(message)
            print(f"Sent: {message}")

            response = await websocket.recv()
            print(f"Received: {response}")

asyncio.run(client())