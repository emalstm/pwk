for ip in $(seq 66 255); do host 38.100.193.$ip; done | grep -v 'not found' | cut -d' ' -f1,5 | cut -d'.' -f1-4,6-13

