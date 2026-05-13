#!/usr/bin/env python3
import os
import subprocess
import sys
import time
from rich.console import Console #type:ignore


console = Console()

def upgrade_all():
    """Upgrade system packages"""
    os.system("sudo apt update && sudo apt upgrade -y")

def install_config_files():
    os.system(f"wget https://raw.githubusercontent.com/creighton-lewis/Environment-FIles/refs/heads/main/.tmux.conf")
    os.system(f"source-file .tmux.conf")
    os.system(f"wget https://raw.githubusercontent.com/creighton-lewis/Environment-FIles/refs/heads/main/.zshrc")
    os.system(f"source ~/.zshrc")

def download_brew():
    """Install Homebrew and add to bashrc"""
    user = os.system("whoami")
    brew_path = f"/home/{user}/.bashrc"
    os.system(f'/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
    os.system(f"echo 'eval \"$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)\"' >> {brew_path}")
    os.system(f"eval \"$(/home/linuxbrew/.linuxbrew/bin/brew shellenv bash)")

def combine_wordlists():
    """Download and combine SecLists wordlists"""
    os.system("mkdir -p ~/wordlists")
    os.chdir("~/wordlists")
    console.print("⚙ Creating comprehensive wordlists...")
    wordlist_url = (
        f"https://raw.githubusercontent.com/danielmiessler/SecLists"
        "/refs/heads/master/Discovery/Web-Content/raft-large-directories.txt"
    )
    os.system(f"curl -s {wordlist_url} | tee dir_wordlist")
    console.print("✅ Wordlist combined successfully")
    os.system("cd ~")
    time.sleep(10)
    os.system("rm -rf ~/wordlists/dir_wordlist")

def install_reconspider():
    os.system("git clone https://github.com/bhavsec/reconspider.git")
    os.system("unzip ReconSpider.zip")
    os.system("python3 ReconSpider.py")

def install_odat():
    """Install Odat"""
    console.print("ℹ Installing Odat...")
    os.system("sudo apt install -y odat")

def install_dovecot():
    """Install Dovecot"""
    os.system("sudo apt install -y dovecot-core dovecot-imapd")

def install_openvas():
    """Install OpenVAS (GVM)"""
    console.print("⚙ Setting up OpenVAS...")
    os.system("sudo apt update && sudo apt install -y gvm")
    os.system("sudo gvm-setup")
    os.system("sudo gvm-check-setup")

def install_dalfox():
    """Install Dalfox"""
    os.system("brew install dalfox")

def install_linpeas():
    """Install Linux PEAS"""
    os.system("curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | bash")

def install_winpeas():
    os.system("curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/winPEAS.exe -o winPEAS.exe")
    os.system("start winPEAS.exe")

def install_sqlmap():
    """Install SQLMap"""
    os.system("sudo apt install -y sqlmap")

if __name__ == "__main__":
    console.print("=" * 50)
    console.print("Starting automation script...")
    console.print("=" * 50)
    
    upgrade_all()
    download_brew()
    combine_wordlists()
    install_reconspider()
    install_odat()
    install_dovecot()
    install_openvas()
    install_dalfox()
    install_linpeas()
    install_winpeas()
    install_sqlmap()
    
    console.print("=" * 50)
    console.print("✅ All installations completed!")
    console.print("=" * 50)
