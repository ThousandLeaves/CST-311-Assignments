# Client.py

# --------------------------------------------
# MAIN CLIENT CODE SHOULD EXIST UP HERE!
# --------------------------------------------

# Testing dictionaries for below calculations
num = 3
rttResult = 99.0009

rttDict = {
    "r_max"  : 0,
    "r_min"  : 0,
    "r_avg"  : 0,
    "rtt1" : 192.11,
    "rtt2" : 42.0112
}

rttDict["rtt" + str(num)] = rttResult

print rttDict.get("rtt3")
########## Min RTT ##########
# Calculated by adding the first recorded RTT as min. Each subsequent RTT
# checks if smaller against the value for min. If true, chg to current RTT
########## Max RTT ##########
# Works just like min RTT but for max instead
########## Avg RTT ##########
# Add the current RTT to this field for each RTT response. Then divide by
# number of successful RTTs
########## Packet loss % ##########
# Simply num of timeouts * 10
########## Estimated RTT ##########
#
# Dev RTT:
#Timeout Interval:

# NOTE::
# Try to avoid using dict structure. We'll get the ERTT and DRTT as
# pings come in
