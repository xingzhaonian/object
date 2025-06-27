import threading
import time

class StoppableThread(threading.Thread):
    def __init__(self, target_func):
        super().__init__()
        self._stop_event = threading.Event() 
        self.target_func = target_func

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        while not self.stopped():
            self.target_func(self.stopped) 

def test(should_stop):
    while not should_stop():
        print('我在工作', should_stop())
        time.sleep(0.1) 


def batch(num):
    for i in range(num):
        thread = StoppableThread(test)
        thread.start()
        # 打印线程信息
        current_thread = threading.current_thread()
        current_thread_id = threading.get_ident()
        thread_count = threading.active_count()
        print(f'当前线程: {current_thread}, id: {current_thread_id}, 线程总数量: {thread_count}')
        thread.stop()
        time.sleep(0.1)
        print('线程已停止')
batch(30)