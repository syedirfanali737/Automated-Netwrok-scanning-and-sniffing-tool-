sudo tcpdump -i eth0 -n -A 'tcp port 21' | grep -E 'USER | PASS '
