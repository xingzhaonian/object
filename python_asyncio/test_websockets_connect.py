import websockets, asyncio

async def test_websocket(url):
    try:
        async with websockets.connect(url, timeout = 3) as ws:
            print('connect success')
            return True
    except:
        print('connect fail')
        return False

asyncio.get_event_loop().run_until_complete(test_websocket('wss://jpgdweb01.37games.com:11100/'))
