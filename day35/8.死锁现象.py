# import time
# from threading import Thread,Lock,RLock
#
# noodle_lock = RLock()
# fork_lock = RLock()
#
# def eat(name):
#     noodle_lock.acquire()
#     print(name,'抢到面了')
#     fork_lock.acquire()
#     print(name, '抢到叉子了')
#     print(name, '吃面')
#     time.sleep(0.1)
#     fork_lock.release()
#     print(name, '放下叉子了')
#     noodle_lock.release()
#     print(name, '放下面了')
#
#
# def eat2(name):
#     fork_lock.acquire()
#     print(name, '抢到叉子了')
#     noodle_lock.acquire()
#     print(name, '抢到面了')
#     print(name, '吃面')
#     fork_lock.release()
#     print(name, '放下叉子了')
#     noodle_lock.release()
#     print(name, '放下面了')
#
# # lst = ['alex','wusir','taibai','大壮']
# Thread(target=eat,args=('alex',)).start()
# Thread(target=eat2,args=('wusir',)).start()
# Thread(target=eat,args=('taibia',)).start()
# Thread(target=eat2,args=('大壮',)).start()




import time
from threading import Thread,Lock,RLock


fork_lock = Lock()

def eat(name):
    fork_lock.acquire()
    print(name,'抢到面了')
    print(name, '抢到叉子了')
    print(name, '吃面')
    time.sleep(0.1)
    fork_lock.release()
    print(name, '放下叉子了')

    print(name, '放下面了')


def eat2(name):
    fork_lock.acquire()
    print(name, '抢到叉子了')

    print(name, '抢到面了')
    print(name, '吃面')
    fork_lock.release()
    print(name, '放下叉子了')

    print(name, '放下面了')

# lst = ['alex','wusir','taibai','大壮']
Thread(target=eat,args=('alex',)).start()
Thread(target=eat2,args=('wusir',)).start()
Thread(target=eat,args=('taibia',)).start()
Thread(target=eat2,args=('大壮',)).start()




# 死锁现象是怎样产生的？
    # 多把锁 并且多个线程中 交叉使用
        # fork_lock.acquire()
        # noodle_lock.acquire()
        #
        # fork_lock.release()
        # noodle_lock.release()

    # 如果是互斥锁，出现了死锁现象，最快速的解决方法把所有的互斥锁都改成一把递归锁
        # 程序的效率会变低
    # 递归锁 效率低 但是解决死锁现象有奇效
    # 互斥锁 效率高 但是多把锁容易出现死锁现象

    # 一把互斥锁就够了