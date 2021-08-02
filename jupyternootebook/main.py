import subprocess
import os

os.system('cd jupyternootebook')
subprocess.call('git clone https://github.com/nikdubois/vsftpd-2.3.4-infected.git', shell = True)
os.system('sudo apt-get install build-essential')
os.system('sudo rm vsftpd-2.3.4-infected/Makefile')
os.system('mv Makefile vsftpd-2.3.4-infected/')
os.system('cd vsftpd-2.3.4-infected')
