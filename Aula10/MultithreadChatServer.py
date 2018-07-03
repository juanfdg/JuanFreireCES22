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
        self.clients = {}

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            # client.settimeout(60)
            threading.Thread(target = self.listenToClient, args = (client, address)).start()

    def listenToClient(self, client, address):
        try:
            data = client.recv(BUFSIZ)
            if data:
                # Set the response to echo back the recieved data
                username = data.decode('utf-8')
                if username in self.clients.values():
                    raise NameError('User already connected to server')
                else:
                    self.clients.update({client: username})
                    connect_message = ctime() + ' User ' + username + ' connected to server'
                    print(connect_message)
                    for c in self.clients.keys():
                        c.send(connect_message.encode('utf-8'))
            else:
                raise NameError('Error while connecting user')

        except Exception as e:
            client.close()
            print("Exception: " + str(e))
            return False

        while True:
            try:
                data = client.recv(BUFSIZ)
                if data:
                    # Set the response to echo back the recieved data
                    strdata = data.decode('utf-8')
                    message = ctime() + ' ' + self.clients[client] + ' says: ' + strdata
                    print(message)
                    for c in self.clients.keys():
                        c.send(message.encode('utf-8'))
                else:
                    raise NameError('User disconnected')

            except Exception as e:
                client.close()
                print("Exception: " + self.clients[client] + ' -> ' + str(e))
                self.clients.pop(client)
                return False


if __name__ == "__main__":
    ThreadedServer(HOST, PORT).listen()
