# 第一件事儿 考试
# 看作业答案
# 登录 上传 下载
# 作业回复

#操作系统的历史
    # 多道操作系统
        # 遇到IO操作就切换的
        # 提高CPU的利用率
        # 进程之间数据隔离
        # 时空复用：在同一个时间点上，多个程序同时执行着，一块内存条上存储了多个进程的数据
    # 分时操作系统
        # 时间分片
        # 时间片轮播

# 进程
    # 是计算机中最小的资源分配单位，每一个程序在运行起来的时候需要给分配一些内存
    # 一个运行的程序
    # 在操作系统中用pid来唯一标识一个进程
# 线程
    # 是计算机中能够被CPU调度的最小单位；实际执行具体编译解释之后的代码是线程，所以CPU执行的是解释之后的线程中的代码
# 并行和并发
    # 并行（好）：多个CPU，各自在自己的CPU上执行多个程序
    # 并发：一个cpu，多个程序轮流执行
# 同步和异步
    # 同步：调用一个操作，要等待结果
    # 异步：调用一个操作，不等待结果
# 阻塞和非阻塞
# 阻塞：CPU不工作
# 非阻塞：CPU工作

# 同步阻塞
    # input sleep recv recvfrom
# 同步非阻塞
    # ret = eval('1+2+3')
# def func(*args):
#     count = 0
#     for i in args:
#         count += 0
#     return count
# a = 1
# b = 2
# c = a + b
# d = func(a,b,c)
# print(d)


# 异步非阻塞(阻塞：setblocking)
# import socket
# sk = socket.socket()
# sk.setblocking(False)
# sk.bind(('127.0.0.1',9000))
# sk.listen()
#
# while 1:
#     try:
#         sk.accept()
#     except BlockingIOError:
#         pass
