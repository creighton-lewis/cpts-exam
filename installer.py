import os 
import subprocess
import sys
import time from rich.console import Console #type: ignore
# Create a console instance – this is what gives us .print() and .input()
console = Console()
os.system("sudo apt update && sudo apt upgrade -y")
#os.system(f'/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
os.system(f"mkdir wordlist")
os.system(f"cd wordlist")
console.print("Creating wordlist for directories, subdomains, files, passwords, and usernames...")
os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/raft-large-words.txt | tee -a dir_wordlist")
os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/raft-small-words.txt | tee -a dir_wordlist")
os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/common.txt | tee -a dir_wordlist")
os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/big.txt | tee -a dir_wordlist")
os.system(f"curl -s https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/raft-large-directories.txt | tee -a dir_wordlist")
console.print("Wordlist for directories, subdomains, files, passwords, and usernames has been created")
os.system(f"cd ~/")
time.sleep(10)
os.system(f"rm -rf dir_wordlist")