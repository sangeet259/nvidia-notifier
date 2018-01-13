import subprocess as sp
import re
import time

# Search for the part we want to get via regex
reg=r"\d+[MiB]+....\d+[MiB]+"



check_time_period=60


while True:
	# get nvidia-smi output
	result=sp.getoutput("nvidia-smi")

	matches = re.findall(reg, result)
	sp.call(['notify-send','GPU-Usage-Status',matches[0]])
	time.sleep(check_time_period)