#!/usr/bin/python

import simulator
import sys
import time

def parse_args(argv):
    rate = pow(int(argv[0]), -1)

    if len(argv) > 1:
        ip = argv[1]
    else:
        ip = None

    if len(argv) > 2:
        port = int(argv[2])
    else:
        port = None

    return rate, ip, port

def usage():
    print("Usage: run_sim.py <rate in Hz>")
    print("Usage: run_sim.py <rate in Hz> <ip>")
    print("Usage: run_sim.py <rate in Hz> <ip> <port>")

def main(argv):
    if len(argv) < 1:
        usage()
    else:
        rate, ip, port = parse_args(argv)

        sim = simulator.Simulator(ip, port)

        while True:
            time.sleep(rate)
            sim.run_once()

if __name__ == "__main__":
    main(sys.argv[1:])