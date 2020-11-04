# import time
# import os
# from threading import Thread,current_thread,enumerate,active_count
# # from multiprocessing import Process as Thread
#
# def func(i):
#     print('start%s'%(i),current_thread().ident)
#     time.sleep(1)
#     print('end%s'%(i))
#
#
# if __name__ == '__main__':
#     t1 = []
#     for i in range(10):
#         t = Thread(target=func,args=(i,))
#         t.start()
#         print(t.ident,os.getpid())
#         t1.append(t)
#     print(enumerate(),active_count())
#     for t in t1:
#         t.join()
#
#     print('所有的线程都执行完了')

# current_thread() 获取当前所在的线程的对象，current_thread().ident通过ident可以获取线程的id
# 线程是不能从外部terminate
# 所有的子进程只能是自己执行完代码之后就关闭
# enumerate 列表 存储了所有活着的线程对象
# active_count 数字 存储了所有活着的线程的个数






# 面向对象的方式起线程
# from threading import Thread
#
# class MyThread(Thread):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         super().__init__()
#
#     def run(self):
#         print(self.ident)
#
# t = MyThread(1,2)
# t.start()
# print(t.ident)






# 线程之间的数据的共享
# from threading import Thread
#
# n = 100
# def func():
#     global n
#     n -= 1
#
# t_1 = []
# for i in range(100):
#     t = Thread(target=func)
#     t.start()
#     t_1.append(t)
#
# for t in t_1:
#     t.join()
#
# print(n)

