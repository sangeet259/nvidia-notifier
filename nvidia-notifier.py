import subprocess as sp
import re
import time
import sys

# Search for the part we want to get via regex
reg=r"\d+[MiB]+....\d+[MiB]+"
reg2=r"\d+"

required_gpu=10 # in MB
check_time_period=30 #seconds



while True:
	# get nvidia-smi output
	# on remote server
	# result=sp.getoutput("nvidia-smi")
	result=sp.getoutput("ssh remote_username@remote_host 'nvidia-smi'")

	matches = re.findall(reg, result)
	
	


	stats=re.findall(reg2,matches[0])

	gpu_free=int(stats[1])-int(stats[0])
	perc_free=100*(1-(int(stats[0])/int(stats[1])))

	perc_free=str(round(perc_free,2))

	if int(stats[1])<required_gpu:
		print("The desired GPU is exceeding the total capacity of this server !!")
		sp.call(['notify-send',"Error !","The desired GPU is exceeding the total capacity of this server !!"])
		sys.exit(1)


	if gpu_free>required_gpu:
		sp.call(['notify-send',perc_free+" %",matches[0]])
		sys.exit(0)


	# make the loop run once every time period
	time.sleep(check_time_period)