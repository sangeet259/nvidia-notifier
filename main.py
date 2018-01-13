import subprocess as sp

# Search for the part we want to get via regex
reg=r"\d+[MiB]+....\d+[MiB]+"

# get nvidia-smi output

result=sp.getoutput("nvidia-smi")

