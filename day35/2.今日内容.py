# Thread
    # 守护线程
# 线程锁 ***** 多个线程之间同时操作全局变量/静态变量 会产生数据不安全现象
    # 互斥锁
    # += -= 说明了线程之间数据的不安全
        # b = a.strip() 带返回值的都是先计算后赋值，数据不安全
        # a = a + 1 \ a += 1 数据不安全
    # append pop 说明了在线程中操作列表的方法是数据安全的
    # if\while 数据不安全
    # 线程安全的单例模式   背下来


    # 递归锁
    # 递归锁和互斥锁的区别
        # 他们的效率
        # 应用场景
    # 死锁现象
        # 死锁现象怎么发生
        # 怎么解决

# 线程队列 主要记用法  get  put  get_nowait
    # 先进先出 Queue
    # 后进先出 LifoQueue
    # 优先级 PriorityQueue


# 线程池进程池 *****