import packet
import socket
import command

class Simulator:
    __ip        = "127.0.0.1"
    __port      = 5005
    __com_port  = 5006
    __state     = 1

    def __init__(self, ip=None, port=None):
        if ip is not None:
            self.__ip = ip
        if port is not None:
            self.__port = port
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.__com_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__com_sock.bind((self.__ip, self.__com_port))
        self.__com_sock.settimeout(0.0)

    def __del__(self):
        self.__sock.close()
        self.__com_sock.close()

    def receive_command(self):
        try:
            com = self.__com_sock.recv(512)
            com = command.Command(com)
            self.__state = com.command
        except:
            pass

    def send_packet(self):
        p                       = packet.Packet()
        p.team_id               = 1
        p.status                = self.__state
        p.position              = 10
        p.velocity              = 20
        p.acceleration          = 0
        p.battery_voltage       = 12
        p.battery_current       = 5
        p.battery_temperature   = 100
        p.pod_temperature       = 1000
        p.stripe_count          = 10000

        self.__sock.sendto(p.pack(), (self.__ip, self.__port))


    def run_once(self):
        self.receive_command()
        self.send_packet()
