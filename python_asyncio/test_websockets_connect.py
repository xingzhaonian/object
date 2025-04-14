import websockets, asyncio

async def test_websocket(url):
    try:
        async with websockets.connect(url, timeout = 3) as ws:
            print('connect success')
            return True
    except:
        print('connect fail')
        return False




#asyncio.get_event_loop().run_until_complete(test_websocket('wss://jpgdweb01.37games.com:11100/'))




def test_websocket_connect(url):
    try:
        websockets.connect(url, timeout = 3)
        print('连接成功')
        return True
    except:
        print('连接失败')
        return False
    
test_websocket_connect('wss://jpgdweb01.37games.com:11100/')