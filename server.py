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

    c.send(bytes("welcome to Nikhil's Server",'utf-8'))

    c.close()
