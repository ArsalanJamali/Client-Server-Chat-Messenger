from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
from tkinter import END


class ServerSocket:

    def __init__(self,receive_block_tk):
        self.socket=None
        self.connection_status=False
        self.receive_block=receive_block_tk
        self.thread=None

    def initiate_connection(self,port):
        port=int(port)
        server_socket=socket(AF_INET,SOCK_STREAM)
        server_socket.bind(('localhost',port))
        server_socket.listen(1)
        print('Server is ready')
        self.socket,_=server_socket.accept() #return a tuple with connection socket and address 
        self.thread=Thread(target=self.receive_handler,args=(self.socket,self.receive_block))
        self.thread.start()


    def receive_handler(self,socket,receive_block):
        self.connection_status=True
        while self.connection_status:
            try:
                receive_message=socket.recv(1024) 
            except:
                break
            receive_block.delete('1.0',END)
            receive_block.insert(END,receive_message.decode())

    def break_connection_status(self):
        self.connection_status=False 
        self.socket.close()
        
    def send_message(self,send_text):
        self.socket.send(send_text.encode())

