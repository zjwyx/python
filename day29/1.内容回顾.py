# 概念
# B/S C/S 架构
    # C/S client server
    # B/S  browser server
# osi七层协议
# 应用层
# 传输层
    # tcp协议：效率低，可靠 ，面向连接\全双工的通信
    # 三次握手
        # 客户端向服务器发送syn请求，
        # 服务器向客户端回复ack并发送syn请求
        # 客户端接收到请求之后再回复ack表示建立连接
        # 由connect+accept
    # 四次挥手
        # 客户端向服务端发送fin请求
        # 服务端回复ack确定
        # 服务端向客户端发送fin请求
        # 客户端回复ack确定
        # 有客户端的close和服务器的close
    # udp协议：不可靠的无连接的 效率高
    # 四层交换机 四层路由器

# 网络层
    # ip协议（ipv4 ipv6）
    # 路由器\交换机
# 数据链路层
    # arp协议  地址解析协议 通过ip找到mac地址
    # 交换机\网卡：单播 广播 组播
# 物理层
