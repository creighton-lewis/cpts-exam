import os 
import sys 
from rich.console import Console #type: ignore
# Create a console instance – this is what gives us .print() and .input()
console = Console()
os.system(f"python3 -m pip install pyftpdlib")
command = input("Enter command: ").strip()
console.print(f"Enter 'start_ftp' to start an FTP server or 'start_http' to start an HTTP server.")
if command == "start_ftp":
    os.system(f"{sys.executable} -m pyftpdlib -p 21 -u user -P pass")
elif command == "start_http":
    try:
        os.system(f"{sys.executable} -m http.server 80 --bind 0.0.0.0")
    except: 
        os.system(f"{sys.executable} -m http.server 8000 --bind 0.0.0.0")
elif command == "start_samba":
   file_check= os.path.exists("/usr/share/doc/python3-impacket/examples/smbserver.py")
   if not file_check:
       console.print("The smbserver.py file is not found. Please install the impacket library to use this feature.")
   os.system(f"sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData Downloads")
else:
    print("Invalid command. Please enter 'start_ftp' or 'start_http'.")