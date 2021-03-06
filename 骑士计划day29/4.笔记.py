# 同一台机器上的两个程序之间的通讯 就需要依赖文件
# 两台机器之间的两个程序之间的通讯 就需要依赖网络


# 两个程序之间的通信：
    # 基于文件的
    # 基于网络的

# 网卡：身份证 mac地址 计算机在网络上的身份证
# 交换机：负责一个网络内的多台机器之间的信息交换
# mac地址：16进制的数，全球唯一
# 区域性
# ip地址
# 4位的点分十进制


# 每台机器有两个地址：ip地址，mac地址
# 全球的主机 都连在了一起

# 局域网
# 网关ip  不同局域网之间通信依赖的ip地址
# 子网掩码  判断两个ip地址是否在同一个网段内
# 网段


# 0.0.0.0 - 255.255.255.255
# 局域网的概念
# 外网ip 我们谁都能访问
# 内网ip 从外面都不能访问，只能在内部环境中互相访问
# 外网ip永远不会和内网ip冲突？
# 0.0.0.0 - 255.255.255.255中间为内网保留了一些字段
# 192.168.0.0 - 192.168.255.255
# 10.0.0.0 - 10.255.255.255
# 172.16.0.0 - 172.31.255.255


# 127.0.0.1 回环地址 指的是在我们的测试过程中使用的一个地址
# 0.0.0.0 开发环境


# 端口的概念 --- 辅助你找到一个应用
# 每一个网络服务都会占用计算机上的一个端口
# 计算机上的端口范围0 - 65535
# 在同一个时刻，同一台计算机上 不同的网络应用 占用的端口一定是不同的



# osi 七层模型
# 应用层   http
# 传输层   TCP,UDP
# 网络层   ip协议
# 数据链路层     arp协议
# 物理层



# tcp 面向连接的 可靠的 但是慢
    # tcp协议
    # 两个应用之间要想通信 必须先建立连接
    # 然后基于连接来通信
    # 比较重要的文件 邮件的发送 下载安装包
# udp 无连接的 快 能够发送的信息长度是有限的
    # 快 但 不可靠 不能发送过长的数据
    # 即使通讯类的程序


# 局域网之间的通信
    # 路由器
    # 网段，子网掩码
    # 网关ip
# 端口
    # 应用到应用

# tcp，udp是通过网络通信的两种方式
    # tcp 先建立连接再通信
        # 可靠
        # 慢
    # udp 不需要建立连接直接通信
        # 快
        # 不可靠