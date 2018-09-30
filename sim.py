import socket
import struct
import time

IP = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

status = 2
acceleration = 10
position = 5
velocity = 30
bat_volt = 12.5
bat_curr = 0.5
bat_temp = 60.5
pod_temp = 100.5

#int32 i
#uint8 B

packet = struct.pack( 'Biiiiiii', status, acceleration, position, velocity, bat_volt, bat_curr, bat_temp, pod_temp )

while 1:
    time.sleep(0.1)
    sock.sendto( packet, (IP, PORT) )

#sock.sendto( packet, (IP, PORT) )
