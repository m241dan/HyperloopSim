import struct

##
# status:
# 0 - fault
# 1 - safe to approach
# 2 - ready to launch
# 3 - launching
# 4 - coasting
# 5 - braking
# 6 - crawling

class Command:
    __com_fmt = 'B'
    command = 5 #might as well default to breaking

    def __init__(self, com):
        #if com == string, unpack it and set it
        #if com == int, set it
        #else just use the default braking
        if isinstance(com, str) and len(com) == struct.calcsize(self.__com_fmt):
            self.command = struct.unpack(self.__com_fmt, com)[0]
        elif isinstance(com, int):
            self.command = com

    def pack(self):
        return struct.pack(self.__com_fmt, self.command)

    def __str__(self):
        return "Command: " + str(self.command)

