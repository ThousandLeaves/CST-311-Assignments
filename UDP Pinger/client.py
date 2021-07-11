# Christopher Boyd
# Client.py (v01)
import time
from socket import *

# Initial variables to set up the UDP client connection
# and point towards a host server and port
serverName = 'hostname'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
i = 1

while i < 11:
    try:
        # Print message of current ping number then send
        # to server
        msg = "Ping" + str(i)
        print("Mesg sent: Ping" + str(i))
        clientSocket.sendto(mesg.encode(),(serverName, serverPort))

        # Begin timer to measure server response
        startTimer = time.time()
        # Get server response as a message
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        # Measure time once again as the end timer point
        endTimer = time.time()
        totalTime = (endTimer - startTimer) * 1000

        # Print response message, followed by ping times and RTT
        print("Mesg rcvd:" + modifiedMessage.decode() + "\n")
        print("Start time: " + str(startTimer) + "\n")
        print("Return time: " + str(endTimer) + "\n")
        print("PONG " + str(i) + "RTT:" + str(totalTime) + "\n")

    except socket.timeout:
        # Packet loss detected, print message informing user
        print("No Mesg rcvd")
        print("PONG " + str(i) + "Request Timed Out")

    # Increment timer and issue second ping
    i += 1

# Close the socket
clientSocket.close()

# Print results of other ping calculations
