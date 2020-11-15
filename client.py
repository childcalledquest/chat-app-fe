import socket

class Socket:
    def __init__(self,host='127.0.0.1', port=65432):
        self.sock = socket.socket()
        self.sock.connect((host,port))
    def get_data(self):
        return self.sock.recv(1024)