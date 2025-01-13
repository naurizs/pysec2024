import urllib.request
import sys,os

#Progresa rādīšanas funkcija
def show_progress(block_num, block_size, total_size):
    progress = (block_num * block_size) / total_size 
       
    barLength = 100 
    status = ""
    progress = float(progress)
    if progress >= 1:
        progress = 1
        status = "Pabeigts...\r\n"
    block = int(round(barLength*progress))
    text = "\rProcenti: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), round((progress*100), 2), status)
    
    sys.stdout.write(text)
    sys.stdout.flush()
    

url = input("Ievadiet URL: ")
name = input("Ievadiet faila nosaukumu: ")
try:
    urllib.request.urlretrieve(url, name, show_progress)   
except KeyboardInterrupt:
    print("\nLejupielāde pārtraukta!")
    os.remove(name)