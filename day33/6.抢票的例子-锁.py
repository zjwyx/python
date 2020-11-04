# import json
# import time
# from multiprocessing import Lock,Process
#
# def search(i):
#     with open('ticket',encoding='utf-8') as f:
#         ticket = json.load(f)
#     print('%s:当前的余票是%s张'%(i,ticket['count']))
#
# def buy_ticket(i):
#     with open('ticket', encoding='utf-8') as f:
#         ticket = json.load(f)
#     if ticket['count'] > 0:
#         ticket['count'] -= 1
#         print('%s买到票了'%i)
#     time.sleep(0.2)
#     with open('ticket',mode='w',encoding='utf-8') as f:
#         json.dump(ticket,f)
#
#
# def get_ticket(i,lock):
#     search(i)
#     # 能够代替acquire和release，并且在此基础上做一些异常处理，保证即使一个进程的代码出错了，也会归还钥匙
#     with lock:
#         buy_ticket(i)
#
#
# if __name__ == '__main__':
#     # 互斥锁
#     lock = Lock()
#     for i in range(10):
#         Process(target=get_ticket,args=(i,lock)).start()











# import time
# from multiprocessing import Lock,Process
#
# def func(i,lock):
#     lock.acquire()  # 拿钥匙  阻塞，等待拿走钥匙的人release
#     print('被锁起来的代码%s'%i)
#     time.sleep(1)
#     lock.release()    # 还钥匙
#
# if __name__ == '__main__':
#     lock = Lock()   # 造锁
#     for i in range(10):
#         p = Process(target=func,args=(i,lock))
#         p.start()




# 互斥锁 不能在同一个进程中连接acqire多次
# from multiprocessing import Lock
# lock = Lock()
# lock.acqire()
# print(1)
# lock.release()
# lock.acqire()
# print(2)
# lock.release()
