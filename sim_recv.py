import socket
import struct

IP = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((IP, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    data = struct.unpack( 'Biiiiiii', data )
    output = ""
    for value in data:
	output += str(value) + "\n"
    print "received message: ", output
