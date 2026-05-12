import os 
#import nmap 
import time
import argparse
from rich.console import Console #type: ignore
console = Console()
parser = argparse.ArgumentParser(prog='myprogram')
def args_help():
    parser.print_help()
    parser.add_argument('--url', type=str, help='The URL to enumerate')
    args = parser.parse_args()
#Actual functions for enumeration
    def web_enumeration(url=args.url): 
        if not url:
            console.print("Please provide a URL to enumerate using the --url argument.")
            return
        try:
            first_curl = os.system(f"curl -s {url}")
        except Exception as e:
            print(f"Error occurred while running curl: {e}") 
            alt_curl = os.system(f"curl -s {url} -I")
        os.system(f"curl -s {url}/robots.txt")
        os.system(f"whois {url} -v")
        os.system(f"nikto -h {url}")
        os.system(f"whatweb {url} -v")
        os.system(f"dig axr {url}")
        os.system(f"whatweb {url} -v")
        os.system(f"nmap -p 80,443 --script=http-title {url} -oN {url}-scan-0")
        os.system(f"nmap -sV --script=http-enum {url} --apend-output -oN {url}-scan-0")
        os.system(f"dig axr {url}")
        os.system(f"nslookup {url}")
    def vuln_scan(url=args.url):
        if not url: 
            console.print("Please provide url")
   

