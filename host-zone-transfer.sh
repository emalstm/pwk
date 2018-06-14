#!/bin/bash

#zone transfer script
#same as dnsrecon -d emalstm.tech -t axfr
#same as dnsenum zonetransfer.me

host -t ns zonetransfer.me | cut -d" " -f4 > nameservers.txt

for url in $(cat nameservers.txt) ; do 
host -l zonetransfer.me $url | grep -v "Transfer failed" |  cut -d" " -f4  > zonetransferoutput.txt;
done
