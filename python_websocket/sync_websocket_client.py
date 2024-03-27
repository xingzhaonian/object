import socket

def send_receive_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8765))

    request = (
        "GET / HTTP/1.1\r\n"
        "Host: localhost:8765\r\n"
        "Connection: Upgrade\r\n"
        "Upgrade: websocket\r\n"
        "\r\n"
    )
    s.sendall(request.encode())

    response = s.recv(1024)
    print(f"收到服务器的HTTP响应:\n{response.decode()}")

    s.sendall("Hello, WebSocket Server!".encode())
    reply = s.recv(1024)
    print(f"收到服务器的回复: {reply.decode()}")

send_receive_message()
