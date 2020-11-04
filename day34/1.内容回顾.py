# 开启进程的另一种方式
# from multiprocessing import Process
# class 类名(Process):
#     def __init__(self,参数):
#         self.属性名 = 参数
#         super().__init__()
#     def run(self):
#         print('子进程要执行的代码')
# p = 类名()
# p.start()

# 守护进程:会等待主进程代码结束之后会立即执行
# p = 类名()
# p.daemon = True    # 守护进程
# p.start()
# 一般情况下，多个进程的执行顺序，可能是：
    # 主进程代码结束 --> 守护进程进程 ---> 子进程结束 --> 主进程结束
    # 子进程结束 --> 主进程代码结束 ---> 守护进程进程 --> 主进程结束

# 锁：保证数据的安全，会降低程序的运行效率（互斥锁）
# from multiprocessing import Lock,Process
# lock = Lock()
# lock.acquire()
# lock.release()
#
# with lock:
#     ...

# 对列  ipc 进程之间通信 --- 数据安全
    # 基于socket\pickle\Lock实现的
    # pipe管道基于socket\pickle\Lock实现的，没有锁数据不安全
from multiprocessing import Queue,Pipe


# 生产者消费者模型
    # 把原本获取数据处理数据的完整过程进行了 解耦
    # 把生产数据和消费数据分开，根据生产和消费的效率不同，来规划生产者和消费者的个数
        # 让程序的执行效率达到平衡

# 如果你写了一个程序，所有的功能\代码都放在一起，不分函数部分类也不分文件
# 解耦合的程序

# 拆分的很清楚的程序
# 松耦合的程序
