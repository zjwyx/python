# from threading import Thread,Lock
#
# n = 0
# def add(lock):
#     for i in range(220000):
#         global n
#         with lock:
#             n += 1
#
# def sub():
#     for i in range(220000):
#         global n
#         with lock:
#             n -= 1
#
# t_1 = []
# lock = Lock()
# for i in range(2):
#     t1 = Thread(target=add,args=(lock,))
#     t1.start()
#     t2 = Thread(target=sub,args=(lock,))
#     t2.start()
#     t_1.append(t1)
#     t_1.append(t2)
# for t in t_1:
#     t.join()
#
# print(n)




# import dis
# a = 0
# def func():
#     global a
#     a += 1
'''
锁
0 LOAD_GLOBAL
2 LOAD_CONST
4 INPLACE_ADD
# GIL锁切换了
6 STORE_GLOBAL
释放锁
'''
# dis.dis(func)





import time
from threading import Thread,Lock

n = []
def append():
    for i in range(220000):
        n.append(1)

def pop(lock):
    for i in range(220000):
        with lock:
            if not n:
                time.sleep(0.00001)
            n.pop()

t_1 = []
lock = Lock()
for i in range(2):
    t1 = Thread(target=append)
    t1.start()
    t2 = Thread(target=pop,args=(lock,))
    t2.start()
    t_1.append(t1)
    t_1.append(t2)
for t in t_1:
    t.join()

print(n)



# 不要操作全局变量，不要在类里操作静态变量
# += -= *= /= if while 数据不安全
# queue logging 数据安全的
