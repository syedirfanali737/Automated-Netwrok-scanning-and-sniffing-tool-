import subprocess
import time

if __name__ == "__main__":
	while True:
		subprocess.run(["clear"])
		print("CREDENTIALS SNIFFING.")
		print("Credentials can potentially be sniffed from any port that is transmitting data in plain text. However, some common ports where credentials may be transmitted in plain text include ")
		print("01. http")
		print("02. ftp")
		print("03. HTTPS/SSH")
		port=int(input("\n\nplease select the above option:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m"))
		print("\n\n\tCREDENTIALS SNIFFING is in progress.")
		print("hit 'ctrl+c' to stop the process.")
		time.sleep(2)
		print(".")
		time.sleep(2)
		print(".")
		time.sleep(2)
		print(".")
		time.sleep(2)
		print(".")
		subprocess.run(["clear"])
		if port==1:
			print("sniffing http credentials...")	
			subprocess.run(["konsole","-e","bash","-c","bash nftcpdump.sh; exec bash"])
		elif port==2:
			print("sniffing ftp credentials...")
			subprocess.run(["konsole","-e","bash","-c","bash credftp.sh; exec bash"])
		elif port==3:
			print("😂️😂️")
			print("sorry, bro there is nothing here. :)")
			break
		else:
			print("../..")			
			break
