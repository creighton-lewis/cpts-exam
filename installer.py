import os 
import subprocess
import sys
import time from rich.console import Console #type: ignore
# Create a console instance – this is what gives us .print() and .input()
console = Console()
def upgrade_all():
    os.system("sudo apt update && sudo apt upgrade -y")
def download_brew():
    user = os.getlogin()
    os.system(f'/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
    os.system(f"echo >> /home/htb-ac-2033367/.bashrc")
    os.system(f"echo 'eval \"$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)\"' >> /home/{user}/.bashrc")
    os.system(f"eval \"$(/home/linuxbrew/.linuxbrew/bin/brew shellenv bash)")
def combine_wordlists():
    os.system(f"mkdir wordlists")
    os.system(f"cd wordlists")
    console.print("Creating wordlist for directories, subdomains, files, passwords, and usernames...")
    os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/raft-large-words.txt | tee -a dir_wordlist")
    os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/raft-small-words.txt | tee -a dir_wordlist")
    os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/common.txt | tee -a dir_wordlist")
    os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/big.txt | tee -a dir_wordlist")
    os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/raft-large-directories.txt | tee -a dir_wordlist")
    console.print("Wordlist for directories, subdomains, files, passwords, and usernames has been created")
    os.system(f"cd ~/")
    time.sleep(10)
    os.system(f"rm -rf wordlists/dir_wordlist")
def install_reconspider():
    os.system(f"wget -O ReconSpider.zip https://academy.hackthebox.com/storage/modules/144/ReconSpider.v1.2.zip")
    os.system(f"unzip ReconSpider.zip")
    os.system(f"python3 ReconSpider.py")
def install_odat():
    console.print("Installing Odat...")
def install_dovecot():
    os.system(f"sudo apt install dovecot-core dovecot-imapd -y")
def install_openvas():
    os.system(f"sudo apt update && sudo apt install gvm -y")
    os.system(f"sudo gvm-setup")
    os.system(f"sudo gvm-check-setup")
def install_dalfox():
    os.system(f"brew install dalfox")
def install_linpeas():
    os.system(f"curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh ")
def install_winpeas():
    os.system(f"curl -L url = https://github.com/peass-ng/PEASS-ng/releases/latest/download/winPEASany_ofs.exe")