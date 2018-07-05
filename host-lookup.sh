for ip in $(cat subdomains.txt); do host $ip.megacorpone.com;done | grep address | cut -d' ' -f1,4

