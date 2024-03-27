import asyncio
import websockets

async def send_receive_message():
    async with websockets.connect("ws://127.0.0.1:8765") as websocket:
        # 不需要手动构造 HTTP 请求
        # 直接发送和接收消息即可
        await websocket.send("Hello, WebSocket Server!")
        reply = await websocket.recv()
        print(f"收到服务器的回复: {reply}")

asyncio.run(send_receive_message())
