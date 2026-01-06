import socket

UDP_IP = ""
UDP_PORT = 5001


class mysock:
    def __init__(self):
        self.msg = "it is none"
        pass

    def create_sock(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def bind_to_ip(self):
        try:
            self.sock.bind((UDP_IP, UDP_PORT))
        except:
            self.sock.close()
            print("lool")

    def tr_listen(self):
        print(f"lissten  {UDP_IP}:{UDP_PORT}")
        data, addr = self.sock.recvfrom(1024)
        self.msg = data.decode()
