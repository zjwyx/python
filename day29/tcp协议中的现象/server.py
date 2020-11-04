import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()
conn.send(b'hell')
conn.send(b'alex')
conn.close()

sk.close()










# 粘包现象
# 只出现在tcp协议中，因为tcp协议 多条消息之间没有边界，并且还有一大堆优化算法
# 发送端：两条消息都很短，发送的间隔时间也非常短
# 接收端：多条消息由于没有及时接受，而在接受方的缓冲推在一起导致的粘包









