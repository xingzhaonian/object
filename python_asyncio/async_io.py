import asyncio
import threading
import time

'''
事件循环

自动检测并执行我们添加给它的任务

任务列表 = [任务a, 任务b, 任务c...]
while True:
    可执行任务列表, 已完成任务列表 = 检测任务列表
    for 任务 in 可执行任务列表:
        执行 任务

    for 任务 in 已经完成的任务列表:
        移除任务
    
    终止时间循环

'''

# python 3.5   async/await

async def f1():
    print('f1 启动>>>', threading.current_thread())
    await asyncio.sleep(1)
    print('f1 结束>>>', threading.current_thread())


async def f2():
    print('f2 启动>>>', threading.current_thread())
    await asyncio.sleep(3)
    print('f2 结束>>>', threading.current_thread())

#task = [f1(), f2()]

#asyncio.run(asyncio.wait(task))

'''
await 后面只能跟可等待对象(携程对象, task对象, future)

普通的同步函数没办法实现异步:
阻塞操作必须替换成相应的异步库提供的函数, 携程函数才能同步进行任务, 如果是同步的函数造成了阻塞, 那么
携程函数只能在原地等待, 等同步的函数结束后, 再去执行其他任务; 换句话说, 就是必须是异步库提供的异步函数
才可以实现任务同步进行, 不在原地等待

await 必须在携程函数中使用, 如果在一个普通的函数内使用await, python会报语法错误

time.sleep() ---> asyncio.sleep()
server.accept() ---> loop.sock
conn.recv ---> loop.sock_recv()

'''

# await 后面只能跟可等待对象,  -- 携程对象
async def recv():
    print('进入io')
    await asyncio.sleep(3)
    print('结束io')
    return 'hello'

async def task1():
    print('task1 启动 >>>')
    data = await recv()
    print('结果',data )
    print('task1 结束 >>>', threading.current_thread())

async def task2():
    print('task2 启动>>>')
    data = await recv()
    print('结果',data )
    print('task2 结束 >>>', threading.current_thread())

#task = [task1(), task2()]
#asyncio.run(asyncio.wait(task))
    

# await 后面只能跟可等待对象,  -- 任务对象
import asyncio

async def nested():
    print('进入 nested io')
    await asyncio.sleep(3)
    print('结束 nested io')
    return 42

async def nested2():
    print('进入 nested 2 io')
    await asyncio.sleep(3)
    print('结束 nested 2 io')
    return 420



async def main(name):
    print(name,'start')
    task1 = asyncio.create_task(nested())
    task2 = asyncio.create_task(nested2())
    print('task 1----', type(task1),task1)
    print('task 2----', type(task2),task2)
    rsult1 = await task1
    resut2 = await task2
    
    print(rsult1)
    print(resut2)

tassk = [main('任务1'), main('任务2')]

asyncio.run(asyncio.wait(tassk))