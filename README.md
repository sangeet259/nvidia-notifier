# nvidia-notifier

### Intro

Tried training your network on the remote server, but there is not enough memory ?

Well I wasted a complete hour checking if it has been freed!

### How ?
It runs a subprocess that calls `nvidia-smi` after every fixed time interval.
From the output it uses regular expression matching to find out the interesting part of the output. 

You can the change the time interval in the code.
You can set the GPU you require so that in only notifies you when the desired amount of GPU is free.


### How to Use ?
1. Add your ssh key to the remote server, here is how to do that : [Add SSH Key](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2)
2. Clone this repo `git clone https://github.com/sangeet259/nvidia-notifier.git`
3. Go to the directory `cd nvidia-notifier`
4. Open the `nvidia-notifier.py` and set the values of <br>
    * `required_gpu` <br> 
    * `check_time_period` <br>
    * `remote_username` <br> 
    * `remote_host`
5. Run `python3 nvidia-notifier.py`


## Important
I could have used [paramiko](http://www.paramiko.org/) so that you just have to pass th password in code itself, 
but to not increase the dependencies I would suggest you add your ssh key in the remote host.
