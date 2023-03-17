import subprocess

if __name__=="__main__":

	IP=input("\n\nspecify the IP address:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
	subprocess.run(["sudo","nmap","-T5","-sV","-O",IP])
