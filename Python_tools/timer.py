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


set_daily_timer(9, 30)  # 每天9:30执行