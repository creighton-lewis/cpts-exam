import sys
import os
import platform 

print(f"os.name is: {os.name}")

if os.name == 'nt':
    print("This is a Windows system.")
elif os.name == 'posix':
    print("This is a Unix-like system (Linux, macOS, etc.).")
else:
    print("Something else entirely.")