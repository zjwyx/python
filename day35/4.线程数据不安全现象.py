from threading import Thread

# n = 0
# def add():
#     for i in range(220000):
#         global n
#         n += 1
#
# def sub():
#     for i in range(220000):
#         global n
#         n -= 1
#
# t_1 = []
# for i in range(2):
#     t1 = Thread(target=add)
#     t1.start()
#     t2 = Thread(target=sub)
#     t2.start()
#     t_1.append(t1)
#     t_1.append(t2)
# for t in t_1:
#     t.join()
#
# print(n)





# import time
#
# n = []
# def append():
#     for i in range(220000):
#         n.append(1)
#
# def pop():
#     for i in range(220000):
#         if not n:
#             time.sleep(0.00001)
#         n.pop()
#
# t_1 = []
# for i in range(2):
#     t1 = Thread(target=append)
#     t1.start()
#     t2 = Thread(target=pop)
#     t2.start()
#     t_1.append(t1)
#     t_1.append(t2)
# for t in t_1:
#     t.join()
#
# print(n)




# += -= *= /= while if 数据不安全  + 和 赋值是分开的两个操作
# append pop strip 数据安全  列表中的方法或者字典中的方法去操作全局变量的时候 数据安全的
# 线程之间也存在数据不安全


# import dis
# a = 0
# def func():
#     global a
#     a += 1
'''
0 LOAD_GLOBAL              0 (a)
2 LOAD_CONST               1 (1)
4 INPLACE_ADD
6 STORE_GLOBAL             0 (a)
'''
# dis.dis(func)




# import dis
# a = []
# def func():
#     a.append(1)
#
# dis.dis(func)
'''
0 LOAD_GLOBAL              0 (a)
2 LOAD_METHOD              1 (append)
4 LOAD_CONST               1 (1)
6 CALL_METHOD              1
8 POP_TOP
'''
