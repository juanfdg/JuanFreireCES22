import socket
import threading
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            # client.settimeout(60)
            threading.Thread(target = self.listenToClient, args = (client, address)).start()

    def listenToClient(self, client, address):
        while True:
            try:
                data = client.recv(BUFSIZ)
                if data:
                    # Set the response to echo back the recieved data
                    strdata = data.decode('utf-8')
                    print(strdata)
                    client.send((ctime() + ' ' + strdata).encode('utf-8'))
                else:
                    raise NameError('Client disconnected')

            except Exception as e:
                client.close()
                print("Exception: " + str(e))
                return False


if __name__ == "__main__":
    ThreadedServer(HOST, PORT).listen()
