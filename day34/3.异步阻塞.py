import requests
from multiprocessing import Process,Queue
url_lst = [
    'https://www.douban.com/doulist/1596699/',
    'https://www.baidu.com'
]


def producer(i,url,q):
    ret = requests.get(url)
    q.put((i,ret.text))

if __name__ == '__main__':
    q = Queue()
    for index,url in enumerate(url_lst):
        Process(target=producer,args=(index,url)).start()
    # join n个进程 n个进程必须都执行完才继续
    for i in range(4):
        print(q.get())



# 同步阻塞
    # 调用函数必须等待结果\cpu没工作
# 同步非阻塞
    # 调用函数必须等待结果\cpu工作 - 调用了一个高计算的函数 strip eval('1+2+3') sum max min
# 异步阻塞
    # 调用函数不需要立即获取结果，而是继续做其他的事情，在获取结果的时候不知道先先获取谁的，但是总之需要等阻塞
# 异步非阻塞
    # 调用函数不需要立即获取结果，也不需要等 start




















