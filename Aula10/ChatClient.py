import threading
from socket import *

HOST = '127.0.0.1' # or 'localhost'
PORT = 21567
BUFSIZ = 1024

tcpCliSock = socket(AF_INET, SOCK_STREAM)
ADDR = (HOST, PORT)
tcpCliSock.connect(ADDR)
host = tcpCliSock.getsockname() # print client host name
print(host)

print('* Enter Username: ')
username = input().encode('utf-8')
tcpCliSock.send(username)
data = tcpCliSock.recv(BUFSIZ)
if data:
    print(data.decode('utf-8'))
messages = []


def receive():
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        print(data.decode('utf-8'))
        messages.append(data.decode('utf-8'))


def send():
    while True:
        data = (input('> ')).encode('utf-8')
        if not data:
            break
        tcpCliSock.send(data)
    tcpCliSock.close()

threading.Thread(target = receive).start()
threading.Thread(target = send).start()