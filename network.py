import socket
import pickle
import ssl


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.check_hostname = False  # Set to True if using a valid SSL certificate with a proper hostname
        context.load_verify_locations("server_cert.pem")  # Path to CA certificate (optional)

        self.client = context.wrap_socket(self.client, server_hostname=self.server)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)