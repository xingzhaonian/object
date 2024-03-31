import websockets
import asyncio
import secrets
import json

msg = {
    'MsgId':10001,
    'Account':'admin',
    'password':123456
}



class WSserver(object):

    def creat_token(self):
        token = secrets.token_hex(12)
        return token


    async def handle(self, websocket, path):
        while True:
            recv_msg = await websocket.recv()
            recv_msg = json.loads(recv_msg)
            print(f"客户端发来的消息: {recv_msg}, 类型是{type(recv_msg)}")
            try:
                if recv_msg['MsgId'] == 10001:
                    if recv_msg['Account'] == 'admin' and recv_msg['password'] == 123456:
                        token = self.creat_token()
                        await websocket.send('验证通过' + str(token))
                    else:
                        await websocket.send('验证未通过')
            except:
                await websocket.send('验证未通过,接收的数据有误, 可能是格式不对, 或者数据类型错误')   
                print('接收的数据有误, 可能是格式不对, 或者数据类型错误')
                continue
    def run(self):
        ser = websockets.serve(self.handle, '192.168.1.12', '9528', ping_interval=None)
        asyncio.get_event_loop().run_until_complete(ser)
        asyncio.get_event_loop().run_forever()

ws = WSserver()
ws.run()

