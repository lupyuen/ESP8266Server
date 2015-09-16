#  Listen to UDP port 9000 and print any message received.
#  Based on https://pymotw.com/2/socket/udp.html

__author__ = 'Luppy'

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to any IP address, port 9000
server_address = ('', 9000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

print >>sys.stderr, '\nwaiting to receive message'
while True:
    data, address = sock.recvfrom(4096)
    print >>sys.stderr, '----received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data
