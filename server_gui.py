import tkinter as tk
from server_setup import ServerSocket

recieved_message=None
server=None


window=tk.Tk()
window.title('Instant LAN Messenger Server')
window.geometry('400x250')
window.resizable(0,0)
window.configure(bg='#ffffff')

port=tk.StringVar()

top_frame=tk.Frame(window,bg='#ffffff')
top_frame.pack(side='left',anchor='nw')
connect_frame=tk.Frame(window,bg='#ffffff')
connect_frame.pack(side='left',anchor='nw')


tk.Label(top_frame,text='Enter port:',font=('Times New Roman',10,'bold'),bg='#ffffff').pack(pady=5,anchor='nw',padx=8)
tk.Entry(top_frame,textvariable=port,borderwidth=3).pack(ipadx=30,padx=8,ipady=5)
connect_status=tk.Label(top_frame,text='Not connected',borderwidth=3,relief='groove',font=('Times New Roman',10),bg='#ffffff',fg='red')
connect_status.pack(pady=5,ipadx=48)

def start_to_listen():
    global server
    server=ServerSocket(recieved_message)
    port_to_initate=port.get()
    server.initiate_connection(port_to_initate)
    connect_status.config(text='Ready Recieve',fg='green')

def send_message_function():
    message=send_message.get('1.0',tk.END)
    server.send_message(message)

def close_socket():
    if server!=None:
        server.break_connection_status()
    window.destroy()

tk.Button(connect_frame,text='Start Listening',command=start_to_listen,borderwidth=6,bg='#ffffff',fg='green',font=('Times New Roman',12,'bold','underline')).pack(pady=[16,8.5],padx=5,ipadx=60,ipady=15)

tk.Label(top_frame,text='Received Message: ',font=('Times New Roman',10,'bold'),bg='#ffffff').pack(pady=5,anchor='nw',padx=8)
recieved_message=tk.Text(top_frame,height=3,width=23,borderwidth=3)
recieved_message.pack(padx=5)

tk.Label(connect_frame,text='Enter Message below: ',font=('Times New Roman',10,'bold'),bg='#ffffff').pack(pady=5,anchor='nw',padx=8)
send_message=tk.Text(connect_frame,height=3,width=40,borderwidth=3)
send_message.pack(padx=5)

tk.Button(connect_frame,text='Send',command=send_message_function,borderwidth=6,bg='#ffffff',fg='green',font=('Times New Roman',12,'bold','underline')).pack(side='right',padx=5,pady=5,ipadx=10,ipady=2)

window.protocol("WM_DELETE_WINDOW", close_socket)
window.mainloop()

