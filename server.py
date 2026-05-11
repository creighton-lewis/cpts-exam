#!/usr/bin/env python3
"""
Simple menu that lets you start either an FTP server (pyftpdlib) or a
basic HTTP server (the built‑in http.server module).

Requirements
------------
pip install rich pyftpdlib
"""

import os
import subprocess
import sys

# Import the Console class (capital C) from the rich library
from rich.console import Console

# Create a console instance – this is what gives us .print() and .input()
console = Console()
def download_required_packages():
    """Install the required packages using pip."""
    cmd = [
        sys.executable, "-m", "pip", "install",
        "rich", "pyftpdlib"
    ]
    console.print("[yellow]Installing required packages …[/]")
    subprocess.run(cmd, check=True)
def start_ftp():
    """Start a temporary FTP server on port 21."""
    # pyftpdlib command line options:
    #  -p <port>            – bind port
    #  -u <username> -P <password> – simple authentication
    cmd = [
        sys.executable, "-m", "pyftpdlib",
        "-p", "21",
        "-u", "user",
        "-P", "pass"
    ]
    console.print("[yellow]Launching FTP server on port 21 …[/]")
    subprocess.run(cmd, check=False)   # runs until you stop it with Ctrl‑C

def start_http():
    """Start a plain HTTP server on port 80."""
    cmd = [
        sys.executable, "-m", "http.server",
        "80",
        "--bind", "0.0.0.0"
    ]
    console.print("[yellow]Launching HTTP server on port 80 …[/]")
    subprocess.run(cmd, check=False)


def main():
    console.print("[green]Server Starting[/]")
    console.print("[green]1. Start FTP Server")
    console.print("[green]2. Start HTTP Server")

    # .input() returns a plain string (no newline)
    command = console.input("[green]Enter number for corresponding command: ").strip()

    if command == "1":
        start_ftp()
    elif command == "2":
        start_http()
    else:
        console.print("[red]Invalid choice – exiting.[/]")
        sys.exit(1)

if __name__ == "__main__":
    # If you really need sudo privileges on macOS / Linux, you can
    # re‑exec the script with sudo, but that is outside the scope of this
    # example.  The important thing is that the *rich* import now works.
    main()
