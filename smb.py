import argparse
import os
import subprocess
import sys
from typing import List

parser = argparse.ArgumentParser("SMB Enumeration")
parser.add_argument("-ip", required=True, help="Target IP address for SMB enumeration")
args = parser.parse_args()
print (args.ip)
# ----------------------------------------------------------------------
# Optional pretty printing – fall back to plain `print` if Rich is missing
# ----------------------------------------------------------------------
try:
    from rich.console import Console  # type: ignore
    console = Console()
    echo = console.print
except Exception:  # pragma: no cover
    echo = print

def smb_enumeration(ip=args.ip): 
    cmd = "smbmap -H " + ip
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        echo(f"[green]SMB Enumeration successful for {ip}[/green]")
        echo(result.stdout)
    else:
        echo(f"[red]SMB Enumeration failed for {ip}[/red]")
        try:
                cmd = "sudo apt install smbmap -y"
                subprocess.run(cmd, shell=True, check=True)
                echo("[green]smbmap installed successfully. Please run the script again.[/green]")
        except subprocess.CalledProcessError:
                echo("[red]Failed to install smbmap. Please install it manually and run the script again.[/red]")
        echo(result.stderr)
if __name__ == "__main__":
    smb_enumeration()