import subprocess
import time

if __name__ == "__main__":
			
		subprocess.run(["ifconfig"])
		iface = input("\nplease specify your interface name:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
		print("\n\n\tSPECIFIC PROTOCOL SNIFFING is in progress")
		print("\n*** NOTE:-WAITE FOR '5-10' MINUTES TO SCAN THE HOST DEVICES IN A NETWORK.")
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
		print("\n\n\tSPECIFIC PROTOCOL SNIFFING is in progress")
		print("\n\n*** NOTE:-WAITE FOR '5-10' MINUTES TO SCAN THE HOST DEVICES IN A NETWORK.")
		print("hit 'ctrl+c' to stop the process.")
		pot=input("please specify the port number:---> ex: 20,80,443 :\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
		a="tcp port"
		fltr=f"{a} {pot}"
		name=input("\n\nplease specify the file name to the output traffic\n\n\t(~/venkatsaisagar@S3N) $ ")
		try:
			subprocess.run(["tshark", "-i", iface,"-f",fltr,"-w",name])
		except KeyboardInterrupt:
			pass
		analyze=input("\n\nWant to analyze the traffic, Yes/y or No/n :\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
		if analyze=="y" or analyze=="Y" or analyze=="yes" or analyze=="Yes" or analyze=="YES":
			print("wait a min")
			subprocess.run(["wireshark",name])
			subprocess.run(["mv",name,"traffic_files"])
			print("\n\nYour file",name ,"is saved in the 'Traffic_files' directory")
		else:
			subprocess.run(["mv",name,"traffic_files"])
			print("By the way","Your file",name ,"is saved in the 'Traffic_files' directory")
			print("Don't worry its safe.")
			print("...")
		
