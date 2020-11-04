# multiple  多元化的
# processing  进程
# multiprocessing   多元的处理进程的模块


# from multiprocessing import Process
# import os
# # pid process id   进程id
# # ppid parent process id  父进程id
#
# def func(name,age):
#     print(os.getpid(),os.getppid(),name,age)
#
#
#
#
#
# if __name__ == '__main__':
#     # 只会在主进程中执行的所有的代码你写在name=main下
#     print('main:',os.getpid(),os.getppid())
#     p = Process(target=func,args=('alex',84))
#     p.start()











# 为什么要用if __name__ == '__main__':
    # a = 1


# 能不能给子进程传递参数
# from multiprocessing import Process
# import os
# # pid process id   进程id
# # ppid parent process id  父进程id
#
# def func(name,age):
#     print(os.getpid(),os.getppid(),name,age)
#
# if __name__ == '__main__':
#     # 只会在主进程中执行的所有的代码你写在name=main下
#     print('main:',os.getpid(),os.getppid())
#     p = Process(target=func,args=('alex',84))
#     p.start()


# 能不能获取子进程的返回值    不能

# 能不能同时开启多个子进程
# from multiprocessing import Process
# import os
# import time
# # pid process id   进程id
# # ppid parent process id  父进程id
#
# def func(name,age):
#     print('%s stsrt' %(name))
#     time.sleep(1)
#     print(os.getpid(),os.getppid(),name,age)
#
#
# if __name__ == '__main__':
#     # 只会在主进程中执行的所有的代码你写在name=main下
#     print('main:',os.getpid(),os.getppid())
#     arg_lst = [('alex',84),('太白', 40),('wusir', 48)]
#     for arg in arg_lst:
#         p = Process(target=func,args=arg)
#         # 异步非阻塞
#         p.start()



# join的用法
# from multiprocessing import Process
# import os
# import time
# import random
#
#
# def func(name,age):
#     print('发送一封邮件给%s岁的%s'%(name,age))
#     time.sleep(random.random())
#     print('发送完毕')
#
#
# if __name__ == '__main__':
#     arg_lst = [('大壮',40),('alex', 84), ('太白', 40), ('wusir', 48)]
#     p_lst = []
#     for arg in arg_lst:
#         p = Process(target=func,args=arg)
#         # 异步非阻塞
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:
#         p.join()
#
#     # p_1 = []
#     # p = Process(target=func, args=('大壮',40))
#     # p.start()
#     # p_1.append(p)
#     # p = Process(target=func, args=('alex', 84))
#     # p.start()
#     # p_1.append(p)
#     # p = Process(target=func, args=('太白', 40))
#     # p.start()
#     # p_1.append(p)
#     # p = Process(target=func, args=('wusir', 48))
#     # p.start()
#     # p.join()
#     print('所有的邮件已经发送完毕')












# 同步阻塞 异步非阻塞
    # 同步阻塞:join
    # 异步非阻塞:start

# 多进程之间的数据是否隔离
# from multiprocessing import Process
# n = 0
# def func():
#     global n
#     n += 1
#
# if __name__ == '__main__':
#     p_1 = []
#     for i in range(100):
#         p = Process(target=func)
#         p.start()
#         p_1.append(p)
#     for p in p_1:
#         p.join()
#     print(n)

# 使用多个进程实现一个并发的socket的server

















