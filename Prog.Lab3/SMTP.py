from socket import *

# Message to send
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Our mail server is smtp.stud.ntnu.no
mailserver = 'smtp.stud.ntnu.no'

# Create socket called clientSocket and establish a TCP connection
# (use the appropriate port) with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
#Fill in end

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
        print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
        print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = 'MAIL FROM: <sindrhan@stud.ntnu.no>\r\n'
clientSocket.send(mailFromCommand)
recv2 = clientSocket.recv(1024)
print recv2
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
RcptToCommand = 'RCPT TO: <sindrhan@stud.ntnu.no>\r\n'
clientSocket.send(RcptToCommand)
recv3 = clientSocket.recv(1024)
print recv3
# Fill in end

# Send DATA command and print server response.
# Fill in start
clientSocket.send('DATA\r\n')
recv4 = clientSocket.recv(1024)
print recv4
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg)
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send('QUIT\r\n')
recv5 = clientSocket.recv(1024)
print recv5
# Fill in end
