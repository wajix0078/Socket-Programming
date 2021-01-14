import socket

class ServerClass:
    def __init__(self):
        self.socket = socket.socket()
        self.host  = socket.gethostname()
        self.port = 12345
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.conn, self.address = self.socket.accept()

    def connectionDetails(self):
        return f"Connection from {self.address}"
    def createConn(self):
        pass