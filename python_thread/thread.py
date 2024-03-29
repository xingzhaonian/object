import threading
import time
def demo1():
    count = 1
    while True:
        time.sleep(1)
        count += 1
        print(f'当前计数{count}')
        thread_id = threading.get_ident()
        print(f'当前线程{thread_id}')

thread = threading.Thread(target=demo1)

