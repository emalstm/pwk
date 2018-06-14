#/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "10.0.0.2" #metasploitable machine
port = 110 #POP3

try:
    print('\nSending evil buffer...')
    s.connect(ip, port)
    data = recv(1024) #receive banner
    print(data) #print banner

    s.send('USER test' +  '\r\n') #send username "test"
    data = s.recv(1024)
    print(data)

    s.send('PASS test' +  '\r\n') #send password "test"
    data = s.recv(1024)
    print(data)

    s.close() #close socket
    print('\nDone')

except:
    print("Could not connect to POP3")
