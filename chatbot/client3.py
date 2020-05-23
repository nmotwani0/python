import socket

c = socket.socket()

c.connect(('localhost',9999))

name = input("Enter your name")
c.send(bytes(name,'utf-8'))

sendto = input("Whom would you like to chat?")
c.send(bytes(sendto,'utf-8'))

print(c.recv(1024).decode())