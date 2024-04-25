import websocket
import json
import time
import threading

class ClientMain(object):
    def __init__(self):
        self.address =  'ws://192.168.1.12:9528/ws'
        self.WebSocket = websocket.create_connection(self.address)
        self.action = None
        self.recv_total = ''

    def recv_data(self):
        while True:
            self.recv_total = self.WebSocket.recv()
            time.sleep(0.1)
    
    def AccountVerification(self, msg):
        msg = json.dumps(msg)
        self.WebSocket.send(msg)
        while self.recv_total == '':
            time.sleep(0.1)
            continue
        recv_msg = self.recv_total
        self.recv_total = ''
        return recv_msg
    
    def quit(self):
        self.WebSocket.close()

c = ClientMain()
recv_data_thread = threading.Thread(target=c.recv_data)
recv_data_thread.start()
