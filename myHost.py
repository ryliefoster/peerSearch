import myData as md
import searchTable as st
import socket

class myHost:
    def __init__(self, HOST, PORT, searchTable):
        self.HOST = HOST
        self.PORT = PORT
        self.searchTable = searchTable
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def run(self):
        self.s.bind((self.HOST, self.PORT))
        self.s.listen()
        conn, addr = self.s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(2048)
                conn.sendall(self.searchTable.search(data))
                conn, addr = self.s.accept()