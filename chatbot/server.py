import socket

s = socket.socket()
print("Socket Created")

s.bind(('localhost',9999))

s.listen(3)

print("waiting for connections")

while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print("Client Connected with ",addr,name)

    c.send(bytes("welcome to J.A.R.V.I.S.",'utf-8'))

    message = c.recv(1024).decode()
    if(message == 'hello'):
        c.send(bytes("What can I do for you?",'utf-8'))
    else:
        c.send(bytes("Hello",'utf-8'))

    c.close()
