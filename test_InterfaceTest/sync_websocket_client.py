import websocket
import json
import time
import threading

class ClientMain(object):
    def __init__(self):
        self.address =  'ws://192.168.1.12:9528/ws'
        self.WebSocket = websocket.create_connection(self.address)
        self.recv_message = ''

    def recv_data(self):
        while True:
            self.recv_message = self.WebSocket.recv()

    def AccountVerification(self, msg):
        msg = json.dumps(msg)
        self.WebSocket.send(msg)
        while self.recv_message == '':
            continue
        recv_msg = self.recv_message
        self.recv_message = ''
        return recv_msg


    def quit(self):
        self.WebSocket.close()


