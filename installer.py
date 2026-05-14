#!/usr/bin/env python3
import os
import subprocess
import sys
import time
import shutil
from rich.console import Console #type:ignore


console = Console()


def upgrade_all():
    """Upgrade system packages"""
    os.system("sudo apt update && sudo apt upgrade -y")

def install_config_files():
    console.print("⚙ Downloading configuration files...")
    base_link="/creighton-lewis/Environment-FIles/refs/heads/main/"
    os.system(f"wget https://raw.githubusercontent.com/{base_link}.tmux.conf")
    os.system(f"source-file .tmux.conf")
    os.system(f"wget https://raw.githubusercontent.com/{base_link}.zshrc")
    os.system(f"mv .zshrc ~/.zshrc")
    os.system(f"source ~/.zshrc")
    os.system(f"https://raw.githubusercontent.com/{base_link}init.lua")
    os.system(f"mv init.lua ~/.config/nvim/init.lua")
    os.system(f"source ~/.config/nvim/init.lua")

def download_brew():
    """Install Homebrew and add to bashrc"""
    user = os.getlogin()
    print(f"Current user: {user}")
    brew_path = f"/home/{user}/.bashrc"
    os.system(f'/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
    try:
        os.system(f"echo 'eval \"$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)\"' >> {brew_path}")
        os.system(f"eval \"$(/home/linuxbrew/.linuxbrew/bin/brew shellenv bash)")
    except:
        console.print("[red]Error adding Homebrew to bashrc. Please add it manually:[/red]")




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
    os.system("curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh")

def install_winpeas():
    os.current_dir = os.getcwd()
    os.system("curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/winPEAS.exe -o winPEAS.exe")

def install_sqlmap():
    """Install SQLMap"""
    os.system("sudo apt install -y sqlmap")

if __name__ == "__main__":
    console.print("=" * 50)
    console.print("Starting automation script...")
    console.print("=" * 50)
    
    upgrade_all()
    download_brew()
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
