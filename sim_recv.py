import socket
import struct
import packet
import time

IP = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((IP, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print( "Receiving..." )
    data = packet.Packet(data)
    print( str(data) )
    print( "Receive Complete at " + str(time.time()) )