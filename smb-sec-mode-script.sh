#!/bin/bash
nmap -iL hostsup.txt --script smb-security-mode > smb-sec-mode.txt
grep 'Host script' -B8 -A6 smb-sec-mode.txt
