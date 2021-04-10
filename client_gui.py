import tkinter as tk
from client_setup import ClientSocket

recieved_message=None
socket=None

window=tk.Tk()
window.title('Instant LAN Messenger Client')
window.geometry('400x250')
window.resizable(0,0)
window.configure(bg='#ffffff')


ip_address=tk.StringVar()

top_frame=tk.Frame(window,bg='#ffffff')
top_frame.pack(side='left',anchor='nw')
connect_frame=tk.Frame(window,bg='#ffffff')
connect_frame.pack(side='left',anchor='nw')



tk.Label(top_frame,text='Enter Ip and port:',font=('Times New Roman',10,'bold'),bg='#ffffff').pack(pady=5,anchor='nw',padx=8)
tk.Entry(top_frame,textvariable=ip_address,borderwidth=3).pack(ipadx=30,padx=8,ipady=5)
connect_status=tk.Label(top_frame,text='Not connected',borderwidth=3,relief='groove',font=('Times New Roman',10),bg='#ffffff',fg='red')
connect_status.pack(pady=5,ipadx=48)


def initiate_connection():
    global socket
    address,port=ip_address.get().split(':')
    print(address,port)
    socket=ClientSocket(recieved_message)
    socket.initiate_connection(address,port)
    connect_status.config(text='**Connected**',fg='green')

def client_send():
    message=send_message.get('1.0',tk.END)
    socket.send_message(message)

def close_socket():
    if socket!=None:
        socket.break_connection_status()
    window.destroy()

tk.Button(connect_frame,text='Connect',command=initiate_connection,borderwidth=6,bg='#ffffff',fg='green',font=('Times New Roman',12,'bold','underline')).pack(pady=[16,8.5],padx=5,ipadx=60,ipady=15)

tk.Label(top_frame,text='Received Message: ',font=('Times New Roman',10,'bold'),bg='#ffffff').pack(pady=5,anchor='nw',padx=8)
recieved_message=tk.Text(top_frame,height=3,width=23,borderwidth=3)
recieved_message.pack(padx=5)

tk.Label(connect_frame,text='Enter Message below: ',font=('Times New Roman',10,'bold'),bg='#ffffff').pack(pady=5,anchor='nw',padx=8)
send_message=tk.Text(connect_frame,height=3,width=40,borderwidth=3)
send_message.pack(padx=5)

tk.Button(connect_frame,text='Send',command=client_send,borderwidth=6,bg='#ffffff',fg='green',font=('Times New Roman',12,'bold','underline')).pack(side='right',padx=5,pady=5,ipadx=10,ipady=2)


window.protocol("WM_DELETE_WINDOW", close_socket)
window.mainloop()

