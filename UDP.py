import socket


class UDP:

    def __init__(self, local_port=7500, port=0000, local_ip='127.0.0.1', ip='127.0.0.1', buffer_size=1024, size=32,
                 timeout=0.1):
        self.size = size
        self.r_data = None
        self.s_data = bytearray([0 for x in range(self.size+1)])
        self.local_port = local_port
        self.port = port
        self.local_ip = local_ip
        self.ip = ip
        self.buffer_size = buffer_size
        self.timeout = timeout
        self.sk = socket.socket(socket.AF_INET,  # Internet
                                socket.SOCK_DGRAM)  # UDP
        self.sk.bind((self.local_ip, self.local_port))

    def Convert(self, value):
        if type(value) == str:
            return bytearray(value, 'utf-8')
        elif type(value) == int:
            return value.to_bytes(self.size, 'big')

        return bytearray(value)

    def send(self, value=None):
        if value is not None:
            if (type(value) != bytes) or (type(value) != bytearray):
                self.s_data = self.Convert(value)
            else:
                self.s_data = value
        self.sk.sendto(self.s_data, (self.ip, self.port))
        print(f'Sent\n {self.s_data}')

    def receive(self):
        self.r_data, addr = self.sk.recvfrom(self.buffer_size)
        print(f'Received\n {self.r_data}')
        return self.r_data
