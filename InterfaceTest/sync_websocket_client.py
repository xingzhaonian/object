import websocket
import json
import time
import threading

class ClientMain(object):
    def __init__(self):
        self.address =  'ws://127.0.0.1:9528/ws'
        self.WebSocket = websocket.create_connection(self.address)
        self.recv_message = ''

    def recv_data(self):
        while True:
            self.recv_message = self.WebSocket.recv()

    def SendMessage(self, msg):
        msg = json.dumps(msg)
        self.WebSocket.send(msg)
        while self.recv_message == '':
            time.sleep(0.1)
            continue
        recv_msg = self.recv_message
        self.recv_message = ''
        return recv_msg


    def quit(self):
        self.WebSocket.close()


