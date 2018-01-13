# nvidia-notifier

### Intro

Tried training your network on the remote server, but there is not enough memory ?

Well I wasted a complete hour checking if it has been freed!

### How ?
It runs a subprocess that calls `nvidia-smi` after every fixed time interval.
From the output it uses regular expression matching to find out the interesting part of the output. 

You can the change the time interval in the code.
You can set the GPU you require so that in only notifies you when the desired amount of GPU is free.

## Important
I could have used [paramiko](http://www.paramiko.org/) so that you just have to pass th password in code itself, 
but to not increase the dependencies I would suggest you add your ssh key in the remote host.
