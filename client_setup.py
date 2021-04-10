from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
from tkinter import END



class ClientSocket:

    def __init__(self,receive_block_tk):
        self.socket=None
        self.receive_block=receive_block_tk
        self.connection_status=False
        self.thread=None

    def initiate_connection(self,ip_address,server_port):
        server_port=int(server_port)
        self.socket=socket(AF_INET,SOCK_STREAM)
        self.socket.connect((ip_address,server_port))
        print('Client Connected')
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

