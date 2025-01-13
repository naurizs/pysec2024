import ftplib
import queue
import threading
from bs4 import BeautifulSoup
import re
import requests

#Funkcija pārbauda vai saits ir pieejams
def test_ftp_availability(ftp_url, running_ftp_sites):
    try:
        ftp = ftplib.FTP(ftp_url, timeout=5)
        ftp.login()  
        ftp.quit()  
        running_ftp_sites.append(ftp_url)
    except ftplib.all_errors as e:
        return False

#Funkcija iegūst sarakstu ar ftp saitiem
def scrape_google(query, num_pages=3):
    results = []
    for page in range(num_pages):
        start = page * 10  
        url = f"https://www.google.com/search?q={query}&start={start}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract links
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and "ftp://" in href:
                match = re.match(r'ftp://([^/]+)', href)
                if match:
                    results.append(match.group(1))
    return results
#Worker funkcija, kas pārbauda vai ftp saiti ir pieejami
def worker_up(site, result_list):
    test_ftp_availability(site, result_list)
    
#Funkcija, kas lasa pirmos 5 failus no ftp saita
def read_first_files(ftp_url):
    try:
        ftp = ftplib.FTP(ftp_url, timeout=2)
        ftp.login()  
        files = []
        ftp.dir(files.append)
        ftp.quit()  
        return files[:5]
    except ftplib.all_errors as e:
        return []


#Worker funkcija, kas lasa failus no ftp saita
def worker(queue):
    while not queue.empty():
        site = queue.get()
        files = read_first_files(site)
        if files:
            print(f"Pirmie pieci faili no {site}:")
            for file in files:
                print(f"  - {file}")
        else:
            print(f"{site} nav atrasti faili.")
        queue.task_done()
        

query = "inurl:ftp -inurl:(http|https)"
print("Meklējam ftp saitus...")
ftp_sites_raw = scrape_google(query, num_pages=5)
ftp_sites = list(set(ftp_sites_raw))
running_ftp_sites = []
print("Pārbaudam kuri no sarakstā esošajiem ftp saitiem ir pieejami...")
threads = []

#Pārbaudam kuri no sarakstā esošajiem ftp saitiem ir pieejami
for site in ftp_sites:
    t = threading.Thread(target=worker_up, args=(site, running_ftp_sites))
    t.start()
    threads.append(t)   

for t in threads:
    t.join()

#Izveidojam rindu ar pieejamajiem ftp saitiem
running_ftp_sites_q = queue.Queue()
print("Pieejamie ftp saiti no saraksta:")
for site in running_ftp_sites:
    print(site)
    running_ftp_sites_q.put(site)

 
threads = []
num_threads = 5
#Ar 5 pavedieniem lasam failus no ftp saitiem
for _ in range(num_threads):
    t = threading.Thread(target=worker, args=(running_ftp_sites_q,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("\nFailu lasīšana pabeigta.") 