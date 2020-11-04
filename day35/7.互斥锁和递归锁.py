# from threading import Lock,RLock
# Lock 互斥锁  效率高
# RLock 递归(recursion)锁  效率相对低

# lock = Lock()
# lock.acquire()
# print('希望被锁住的代码')
# lock.release()


# 在同一个线程可以被acquire多次
# r1 = RLock()
# r1.acquire()
# print('希望被锁住的代码')
# r1.release()







# from threading import Thread,RLock
#
# def func(i,lock):
#     lock.acquire()
#     print(i,':start')
#     lock.release()
#     print(i, ':end')
#
# lock = RLock()
# for i in range(5):
#     Thread(target=func,args=(i,lock)).start()




























