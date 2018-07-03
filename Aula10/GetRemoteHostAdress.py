import socket


def get_remote_machine_info():
    remote_host = 'www.ita.br'
    print("IP address: %s" % socket.gethostbyname(remote_host))


if __name__ == '__main__':
    get_remote_machine_info()
