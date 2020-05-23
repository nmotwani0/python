import socket

c = socket.socket()

c.connect(('localhost',9999))

name = input("Enter your name")
c.send(bytes(name,'utf-8'))

message = input("Do you want to chat(y/n):")
if(message == 'y'):

    while True:
        mess = input("Enter messsage")
        c.send(bytes(mess,'utf-8'))
        print(c.recv(1024).decode())
        print(c.recv(1024).decode())
        print("abcd")