import subprocess
import time

if __name__ == "__main__":
    
    print("*** NOTE:-	WAITE FOR '5-10' MINUTES TO SNIFF THE NETWORK.")
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
    print("*** NOTE:-	WAITE FOR '5-10' MINUTES TO SNIFF THE NETWORK.")
    print("hit 'ctrl+c' to stop the process.")
    print("\n\n")
    subprocess.run(["ifconfig"])
    iface = input("please specify your interface name:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
    name = input("\n\nplease specify the file name to the output traffic:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
    try:
        subprocess.run(["tshark", "-i", iface, "-f", "broadcast", "-w", name])
    except KeyboardInterrupt:
        pass
    analyze=input("\n\nWant to analyze the traffic, Yes/y or No/n :\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
    if analyze=="y" or analyze=="Y" or analyze=="yes" or analyze=="Yes" or analyze=="YES":
    	print("wait a min")
    	subprocess.run(["wireshark",name])
    	subprocess.run(["mv",name,"traffic_files"])
    	print("Your file",name ,"are saved in the 'Traffic_files' directory")
    else:
    	subprocess.run(["mv",name,"traffic_files"])
    	print("By the way","Your file",name ,"is saved in the 'Traffic_files' directory")
    	print("Don't worry its safe.")
    	print("...")
