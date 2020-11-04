import time
class A:
    from threading import Lock
    __instance = None
    lock = Lock()
    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                # cpu进行轮转
                time.sleep(0.000001)
                cls.__instance = super().__new__(cls)
        return cls.__instance

def func():
    a = A()
    print(a)

from threading import Thread
for i in range(10):
    Thread(target=func).start()
