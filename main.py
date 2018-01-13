import subprocess as sp
import re
import time
import sys

# Search for the part we want to get via regex
reg=r"\d+[MiB]+....\d+[MiB]+"


check_time_period=60


while True:
	# get nvidia-smi output
	result=sp.getoutput("nvidia-smi")

	matches = re.findall(reg, result)
	
	reg2=r"\d+"


	stats=re.findall(reg2,matches[0])

	gpu_free=int(stats[1])-int(stats[0])
	perc_free=100*(1-(int(stats[0])/int(stats[1])))

	perc_free=str(round(perc_free,2))

	if gpu_free>1000:
		sp.call(['notify-send',perc_free+" %",matches[0]])
		sys.exit(0)


	# make the loop run once every time period
	time.sleep(check_time_period)