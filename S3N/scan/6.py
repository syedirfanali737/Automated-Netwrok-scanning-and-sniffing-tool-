import subprocess

if __name__=="__main__":
	IP=input("\n\nspecify the IP address:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")

	print("Testing inside newtwork target")
	print("Targets Ip is which class, exapmle: 198.230.45.67---> This IP belongs to 'CLASS C'")
	print("Class A ---> 1-126   ex:-  1.0.0.0===>126.0.0.0")
	print("Class B ---> 128-191 ex:-  128.0.0.0===>191.0.0.0")
	print("Class C ---> 192-223 ex:-  192.0.0.0===>23.0.0.0")
	cls=input("\n\n\nTargets Ip is which class:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
	if cls=="A" or cls=="a":
		netip=IP+"/8"
		subprocess.run(["sudo","nmap",netip])
		print("ok")

	elif cls=="B" or cls=="b":
		netip=IP+"/16"
		subprocess.run(["sudo","nmap",netip])
		print("ok")

	elif cls=="C" or cls=="c":
		netip=IP+"/24"
		subprocess.run(["sudo","nmap",netip])
		print("ok")
