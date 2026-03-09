import requests
import os
import argparse
import pyfiglet

# ---------------BANNER---------------------
print(pyfiglet.figlet_format(text="httpon",font="larry3d"),end="")
print("")
print("           https://github.com/davidoberst",end="")
print("\n" + "-"*60 + "\n")


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", required=True, help="Ruta de la wordlist") 
args = parser.parse_args()


if not os.path.exists(args.domain):
    print(f"[!] file '{args.domain}' not founded")
    exit()

with open(args.domain, "r") as domains:
    for line in domains:
        url = line.strip()
        if not url: continue 
       
        if not url.startswith("http"):
            url = f"http://{url}"
        
        try:
            response = requests.get(url, timeout=5)
            print(f"\n--- {url} ---")
            print(f"STATUS CODE : {response.status_code}")
            try:
                print("CONTENT (JSON):")
                print(response.json())
            except requests.exceptions.JSONDecodeError:
                print("CONTENT (TEXT):")
                print(response.text[:200]) 
                
        except requests.exceptions.RequestException as e:
            print(f"\n[!] Error conecting {url}: {e}")



