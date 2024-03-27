import asyncio
import websockets

async def handle_http_upgrade(reader, writer):
    data = await reader.readuntil(b"\r\n\r\n")
    headers = data.decode()

    response = (
        "HTTP/1.1 101 Switching Protocols\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        "\r\n"
    )
    writer.write(response.encode())
    await writer.drain()

    # WebSocket 握手是由 websockets 模块自动完成的，不需要手动调用 handshake 函数

async def handle_websocket(websocket, path):
    async for message in websocket:
        print(f"收到客户端消息: {message}")
        await websocket.send(f"服务器已收到你的消息: {message}")

async def main():
    server = await asyncio.start_server(handle_http_upgrade, '127.0.0.1', 8765)

    async with server:
        await server.serve_forever()

asyncio.run(main())
