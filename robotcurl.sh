#!/bin/bash

for ip in $(cat webservers.txt); do
    disallowed=$(curl $ip/robots.txt | grep 'Disallow' -A 10 -B10 | cut -d ' ' -f 2)
    for url in $disallowed; do
        echo "$ip $url"
    done
done
