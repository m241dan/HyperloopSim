import packet
import socket

class Simulator:
    __ip        = "127.0.0.1"
    __port      = 5005

    def __init__(self, ip=None, port=None):
        if ip is not None:
            self.__ip = ip
        if port is not None:
            self.__port = port
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run_once(self):
        p                       = packet.Packet()
        p.team_id               = 1
        p.status                = 2
        p.position              = 10
        p.velocity              = 20
        p.acceleration          = 0
        p.battery_voltage       = 12
        p.battery_current       = 5
        p.battery_temperature   = 100
        p.pod_temperature       = 1000
        p.stripe_count          = 10000

        self.__sock.sendto(p.pack(), (self.__ip, self.__port))