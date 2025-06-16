import datetime
import threading


import threading
import time
from datetime import datetime, timedelta

def daily_task():
    print(f"任务执行时间: {datetime.now()}")
    # 设置明天的同一时间再次执行
    set_daily_timer()

def set_daily_timer(hour=9, minute=30):
    now = datetime.now()
    # 计算下一次执行时间
    next_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if now >= next_time:
        next_time += timedelta(days=1)
    
    delay = (next_time - now).total_seconds()
    print(f"下次执行将在 {next_time} (约{delay/3600:.2f}小时后)")
    
    timer = threading.Timer(delay, daily_task)
    timer.start()


# set_daily_timer(9, 30)  # 每天9:30执行

def test_do():
    now_time = datetime.now()
    active_threads = threading.enumerate()
    print(f"当前线程数量: {len(active_threads)}")
    print(f'函数执行了, 执行时间       {now_time}')
    every_minute()


def every_minute(min = 1):
    now_time = datetime.now()
    print('当前时间',                  now_time)
    next_time = now_time + timedelta(seconds=3)
    delay = (next_time - now_time).total_seconds()
    timer = threading.Timer(delay, test_do)
    timer.start()
    
every_minute()