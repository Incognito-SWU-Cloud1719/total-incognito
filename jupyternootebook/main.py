import subprocess
import os

os.system('cd jupyternootebook')
subprocess.call('git clone https://github.com/nikdubois/vsftpd-2.3.4-infected.git', shell = True)
os.system('sudo apt-get install build-essential')
os.system('cp -f /vsftpd-2.3.4-infected/Makefile Makefile')
os.system('cd vsftpd-2.3.4-infected')