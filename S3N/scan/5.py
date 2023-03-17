import subprocess

if __name__=="__main__":

	IP=input("\n\nspecify the IP address:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
	print("1. Decoy scan.")
	print("2. Packet fragmentation.")
	print("3. Port spoof scan.")
	s_ty=int(input("\n\nplease select the above option:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m"))
	if s_ty==1:
		print("starting DECOY scan, bypassing firewall.*** *** ***")
		subprocess.run(["sudo","nmap","-D","8.8.8.8,20.84.181.62,185.220.101.54,23.129.64.147,185.220.101.82","-vv",IP])

	elif s_ty==2:
		print("starting Packet fragmentation, by Spoofing source address.")
		subprocess.run(["nmap","-f",IP])
		subprocess.run(["nmap","-f","16",IP])
		subprocess.run(["nmap","-f","8",IP])
		subprocess.run(["nmap","-f","4",IP])
		subprocess.run(["nmap","-f","2",IP])
		subprocess.run(["nmap","-f","1",IP])
	
	elif s_ty==3:
		print("starting Port spoof scan, ")
		subprocess.run(["nmap","-g","80", IP])
		res=input("\n\nAre you satisfied with outcome; yes or no:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
		if res=="yes" or res=='YES' or res=='Yes':
			print("\n\nTHANKS")
		elif res=="no" or res=="NO" or res=="No":
			subprocess.run(["nmap","-g","443",IP])
			res1=input("\n\nAre you satisfied with outcome; yes or no:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
			if res1=="yes" or res1=='YES' or res1=='Yes':
				print("\n\nTHANKS")
			elif res1=="no" or res1=="NO" or res1=="No":
				subprocess.run(["nmap","-g","1900",IP])
				res2=input("\n\nAre you satisfied with outcome; yes or no:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
				if res2=="yes" or res2=='YES' or res2=='Yes':
					print("\n\nTHANKS")
				elif res2=="no" or res2=="NO" or res2=="No":
					subprocess.run(["nmap","-g","2869",IP])
					res3=input("\n\nAre you satisfied with outcome; yes or no:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
					if res3=="yes" or res3=='YES' or res3=='Yes':
						print("\n\nTHANKS")
					elif res3=="no" or res3=="NO" or res3=="No":
						subprocess.run(["nmap","-g","7671",IP])
						res4=input("\n\nAre you satisfied with outcome; yes or no:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
						if res4=="yes" or res4=='YES' or res4=='Yes':
							print("\n\nTHANKS")
						elif res4=="no" or res4=="NO" or res4=="No":
							subprocess.run(["nmap","-g","8443",IP])
							print("\n\n\n\tThats it...")
