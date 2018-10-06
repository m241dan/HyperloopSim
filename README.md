# HyperloopSim

This package runs with python 2.7 (you'll find issues with socket on 3.5).

**Usage:**

- _Run the Simulator_: run_simulator.py <rate in Hz> <ip>(optional) <port>(optional) [recommend using default and not putting in ip and port]
- _Run the Receiver_: sim_recv.py [is not configurable and will use default of the simulator]
- _Send a Command_: send_command.py <1-256> [sends on default ip and command port, not configurable yet]

**Details**
- IP: by default everything is localhost( "127.0.0.1")
- Port:
  - For Commands 5006 by default
  - For Packets 5005 by default
  
**Classes**
- simulator.py
  - **constructor()** Takes (ip, port) but will use default values if not passed. Currently recommending defaults.
  - **receive_command()** Attempts to receive a command if there is one there. Will not block.
  - **send_packet()** Sends a spoof packet.
  - **run_once()** Attempts to receive a command and then send a packet [recommended interface to class]
- packet.py
  - **contructor()** Takes either nothing or a string to unpack using struct.
  - **pack()** Returns a string packed with the values set in the packet. Ready to be sent over python2.7 socket.
  - **unpack()** Unpacks a passed string value into it and return the output as a tuple.
  - **__str__()** Returns a string of the current values in a human readable format.
- command.py
  - **constructor()** Takes either a string to unpack for its value or an actual value itself (1-256 byte value)
  - **pack()** Returns a string packed with the values set in the command. Ready to be sent over python2.7 socket.
  - **__str__()** Returns a string of the current values in a human readable format.

**Scripts**
- _run_simulator.py_:
This is a simulator for our pod/sling. It broadcasts fake packets and receives commands.
- _sim_recv.py_:
This is a simple echo listening that just echos out packets for making sure the value they are outputting is correct.
- _send_command.py_:
This script sends command of 1-256 over the default ip and default command socket.
