#!/bin/bash

for ip in $(cat upip.txt) do
nmap -sT $ip -p 25
grep -B 4 open 
cut -d$"\n" -f1,5
done
