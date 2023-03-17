import subprocess

if __name__=="__main__":

	IP=input("\n\nspecify the IP address:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
	while True:
		print("\n\n\nA. Specific port.")
		print("B. Ports range.")
		print("C. All ports.")
		ports=input("\n\nplease select the above option:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
		if ports=="A" or ports=="a":
			s_prt=input("\n\nspecify any port number:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
			a="-p"+s_prt
			subprocess.run(["sudo","nmap",a,"-sV",IP])
		elif ports=="B" or ports=="b":
			s_prt=input("\n\nSpecify port range.{example:- 10-50}:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
			a="-p"+s_prt
			subprocess.run(["sudo","nmap",a,"-sV",IP])
		elif ports=="C" or ports=="c":
			subprocess.run(["sudo","nmap","-p-",IP])
		else:
			print("\n\nusshuu; see the screen properly, is there any option",ports,"above")
			break
