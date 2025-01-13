import time
import requests
import threading

#Funkcija mēra cik ātri lapa atgriež atbildi ar pirmās lapas HTML saturu, šis nav reālais lapas ielādes laiks ar visu html koda izpildīšanu un papildus resursu ielādēšanu
def load_time(url):
    try:
            
        start_time = time.time()  

        response = requests.get(url)

        end_time = time.time()
        duration = end_time - start_time
        
        url_without_https = url.replace('https://','')
        if (response.status_code>=200 and response.status_code<300):
            print(f"Lapa {url_without_https} ielādējās {duration} sekundēs")    
        else:
            print(f"Lapas {url_without_https} ielāde neizdevās, statusa kods: {response.status_code}")
    except Exception as e:
        print(f"Kļūda piekļūstot {url}: {e}")
    
url=['https://valmierasnovads.lv', 'https://valmierasmuzejs.lv', 'https://visit.valmiera.lv', 'https://biblioteka.valmiera.lv', 'https://online.valmierasmuzejs.lv']

threads = []
for site in url:
    thread = threading.Thread(target=load_time, args=(site,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()