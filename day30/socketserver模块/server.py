import time
import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while 1:
            try:
                content = conn.recv(1024).decode('utf-8')
                conn.send(content.upper().encode('utf-8'))
                time.sleep(0.5)
            except ConnectionAbortedError:
                break

server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
server.serve_forever()






# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
#
# while 1:
#     conn,addr = sk.accept()
#     while 1:
#         try:
#             content = conn.recv(1024).decode('utf-8')
#             conn.send(content.upper().encode('utf-8'))
#             time.sleep(0.5)
#         except ConnectionAbortedError:
#             break
