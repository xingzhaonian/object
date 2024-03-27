import websockets

def handle_http_upgrade(reader, writer):
    data = reader.readuntil(b"\r\n\r\n")
    headers = data.decode()

    response = (
        "HTTP/1.1 101 Switching Protocols\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        "\r\n"
    )
    writer.write(response.encode())
    writer.flush()

    websocket = websockets.streams.StreamReader(reader), websockets.streams.StreamWriter(writer)
    return websocket

def handle_websocket(websocket, path):
    while True:
        message = websocket[0].readline()
        print(f"收到客户端消息: {message}")
        websocket[1].write(f"服务器已收到你的消息: {message}\n".encode())
        websocket[1].flush()

server = websockets.server.serve(handle_http_upgrade, 'localhost', 8765)
websockets.server.serve_forever(server)