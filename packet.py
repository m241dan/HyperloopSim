import struct

##
# Packet Structure
#
# uint8     (B) team_id
# uint8     (B) status
# int32     (i) position
# int32     (i) velocity
# int32     (i) acceleration
# int32     (i) battery voltage
# int32     (i) battery current
# int32     (i) battery temperature
# int32     (i) pod temperature
# uint32    (I) stripe_count
#

##
# status:
# 0 - fault
# 1 - safe to approach
# 2 - ready to launch
# 3 - launching
# 4 - coasting
# 5 - braking
# 6 - crawling

class Packet:
    team_id             = 0
    status              = 0
    position            = 0
    velocity            = 0
    acceleration        = 0
    battery_voltage     = 0
    battery_current     = 0
    battery_temperature = 0
    pod_temperature     = 0
    stripe_count        = 0

    __packet_format = 'BBiiiiiiiI'

    def __init__(self, str = None):
        if str is not None and len(str) == struct.calcsize(self.__packet_format):
            packet = struct.unpack(self.__packet_format, str)
            self.team_id                = packet[0]
            self.status                 = packet[1]
            self.position               = packet[2]
            self.velocity               = packet[3]
            self.acceleration           = packet[4]
            self.battery_voltage        = packet[5]
            self.battery_current        = packet[6]
            self.battery_temperature    = packet[7]
            self.stripe_count           = packet[8]
    def unpack(self, str):
        ret = None
        if len(str) == struct.calcsize(self.__packet_format):
            ret = struct.unpack(self.__packet_format, str)
        return ret

    def pack(self):
        return struct.pack(self.__packet_format, self.team_id, self.status, self.position,
                            self.velocity, self.acceleration, self.battery_voltage,
                            self.battery_current, self.battery_temperature, self.pod_temperature,
                            self.stripe_count)
    def __str__(self):
        tostr  = "Team ID            : " + str(self.team_id) + "\n"
        tostr += "Status             : " + str(self.status) + "\n"
        tostr += "Position           : " + str(self.position) + "\n"
        tostr += "Velocity           : " + str(self.velocity) + "\n"
        tostr += "Acceleration       : " + str(self.acceleration) + "\n"
        tostr += "Battery Voltage    : " + str(self.battery_voltage) + "\n"
        tostr += "Battery Current    : " + str(self.battery_current) + "\n"
        tostr += "Battery Temperature: " + str(self.battery_temperature) + "\n"
        tostr += "Pod Temperature    : " + str(self.pod_temperature) + "\n"
        tostr += "Stripe Count       : " + str(self.stripe_count)
        return tostr
