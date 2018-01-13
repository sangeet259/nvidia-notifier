import subprocess as sp
import re

# Search for the part we want to get via regex
reg=r"\d+[MiB]+....\d+[MiB]+"

# get nvidia-smi output

result=sp.getoutput("nvidia-smi")

matches = re.findall(reg, result)

sp.call(['notify-send','GPU-Usage-Status',matches[0]])