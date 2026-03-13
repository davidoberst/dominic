import requests
import os
import argparse
import pyfiglet
import colorama

#----banner
print("")
print("")
print(pyfiglet.figlet_format(text="dominic",font="smblock"),end="")
print("domain status check")
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", required=True, help="wordlist path") 
args = parser.parse_args()



#----logic
if not os.path.exists(args.domain):
    print(f"[!] '{args.domain}' not found.")
    exit()
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
active_urls = []
nonactive = []
with open(args.domain, "r") as domains:
    print("="*50)
    print("[INFO] Requesting domains...")
    print("="*50)
    for line in domains:
        url = line.strip()
        if not url: continue       
        if not url.startswith("http"):
            url = f"https://{url}"
        try:
         response = requests.get(url, timeout=5, headers=headers)
         if response.ok:
            active_urls.append(f"[:] {url} - {response.status_code}")
         else:
            nonactive.append(f"[!] {url} - {response.status_code}")
        except:
           nonactive.append(f"[!] {url} - FAILED/TIMEOUT")

#----results
for x in active_urls:
   print(x)
   
for y in nonactive:
   print(y)

print("="*50)

           


        

