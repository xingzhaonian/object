import time

def demo1():
    
    def washing1():
        time.sleep(3)
        print('第一台洗衣机工作完成, 请取出衣物')

    def washing2():
        time.sleep(2)
        print('第二台洗衣机工作完成, 请取出衣物')

    def washing3():
        time.sleep(5)
        print('第三台洗衣机工作完成, 请取出衣物')

    washing1()
    washing2()
    washing3()


def demo2():

    async def washing1():
        time.sleep(3)
        print('第一台洗衣机工作完成, 请取出衣物')

    async def washing2():
        time.sleep(2)
        print('第二台洗衣机工作完成, 请取出衣物')

    async def washing3():
        time.sleep(5)
        print('第三台洗衣机工作完成, 请取出衣物')
    
    washing1()
    washing2()
    washing3()


def demo3():

    async def washing1():
        await time.sleep(3)
        print('第一台洗衣机工作完成, 请取出衣物')

    async def washing2():
        await time.sleep(2)
        print('第二台洗衣机工作完成, 请取出衣物')

    async def washing3():
        await time.sleep(5)
        print('第三台洗衣机工作完成, 请取出衣物')

    washing1()
    washing2()
    washing3()



import asyncio 

start_time = time.time()
async def washing1():
    await asyncio.sleep(3)
    print('第一台洗衣机工作完成, 请取出衣物')

async def washing2():
    await asyncio.sleep(2)
    print('第二台洗衣机工作完成, 请取出衣物')

async def washing3():
    await asyncio.sleep(5)
    print('第三台洗衣机工作完成, 请取出衣物')

# 创建事件循环对象
event_loop_object = asyncio.get_event_loop()

task = [washing1(), washing2(), washing3()]

event_loop_object.run_until_complete(asyncio.wait(task))

event_loop_object.close()
end_time = time.time() - start_time
print('用时', end_time)

