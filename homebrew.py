import os 
import sys 
import subprocess
import time
def download_brew():
    """Install Homebrew and add to bashrc"""
    user = os.system("whoami")
    print(user)
    time.sleep(5)
    brew_path = f"/home/{user}/.bashrc"
    print (brew_path)
    os.system(f'/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
    os.system(f"echo 'eval \"$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)\"' >> {brew_path}")
    os.system(f"eval \"$(/home/linuxbrew/.linuxbrew/bin/brew shellenv bash)")
download_brew()