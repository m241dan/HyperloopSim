#!/usr/bin/python

import command
import socket
import sys

def usage():
    print( "send_command.py <com value(1-256)>")

def main(argv):
    if len(argv) != 1:
        usage()
    else:
        com = command.Command(int(argv[0]))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(com.pack(), ("127.0.0.1", 5006))

if __name__ == "__main__":
    main(sys.argv[1:])