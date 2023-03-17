clear
ifconfig
echo "Enter the interface name:"
read iface
sudo tcpdump -i $iface -n -A 'tcp port 80 and (tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354)'
