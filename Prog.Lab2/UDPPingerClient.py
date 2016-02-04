import time
from socket import *

# Get the server hostname and port as command line arguments                    
host = '127.0.0.1'
port = 12000
timeout = 1 # in seconds
 
# Create UDP client socket
# FILL IN START		
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(timeout)

# FILL IN END

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent as in the Lab description	
    data = "Ping "+str(ptime)+ " "
    try:
    	# FILL IN START
    	
	# Record the "sent time"
        sendTime = time.time()
        data += str(sendTime)
        
	# Send the UDP packet with the ping message
        clientSocket.sendto(data, (host, port))

        # Receive the server response
        message, address = clientSocket.recvfrom(2048)

        # Record the "received time"
        recvTime = time.time()

        # Display the server response as an output
        print message
	# Round trip time is the difference between sent and received time
        RTT = recvTime - sendTime
        print "RTT: "+str(RTT)
        
        # FILL IN END
    except:
        # Server does not response
	# Assume the packet is lost
        print "Request timed out."
        continue
 
# Close the client socket
clientSocket.close()
 
