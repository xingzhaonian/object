import asyncio
import websockets

async def main():
    async with websockets.connect("ws://localhost:8765") as websocket:
        message = "Hello, server!"
        await websocket.send(message)
        print(f"Sent: {message}")

        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(main())