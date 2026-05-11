import os 
import nmap 
url="http://walmart.com"
def get_web_info():
    os.system(os.system(f"curl -s {url}"))
    os.system(f"whois {url} -v")
    os.system(f"nslookup {url}")
    os.system(f"whatweb {url} -v")
    os.system(f"nmap -p 80,443 --script=http-title {url} -oN {url}-scan-0")
    os.system(f"nmap -sV --script=http-enum {url} --apend-output -oN {url}-scan-0")
    os.system(f"")
    os.system