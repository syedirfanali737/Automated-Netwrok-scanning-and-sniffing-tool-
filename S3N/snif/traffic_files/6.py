import subprocess 
import time

if __name__=="__main__":
	while True:
		print("")
		print("")
		subprocess.run(["ls"])
		fils=input("\n\nplease specify your file name to analyze, from above list: Don't include {'6.py' or '6.sh'} file..:\n\n\t\033[31m(~/venkatsaisagar@S3N) $ \033[0m")
		if fils=="6.sh" or "6.py":
			print("arey thuupass eydhava, oddu aaanna kadhana.")
			print("Idiot, check your eyes, read the above sentence properly.")
			time.sleep(5)
			subprocess.run(["clear"])
			continue
		else:
			subprocess.run(["wireshark",fils])
			subprocess.run(["clear"])
