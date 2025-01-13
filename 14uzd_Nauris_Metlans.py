from scapy.all import IP, TCP, sr1
import multiprocessing
import ipaddress

def scan_port(ip, port):
    try:
        syn_packet = IP(dst=ip) / TCP(dport=port, flags="S")
        response = sr1(syn_packet, timeout=1, verbose=0)
        if response is not None and TCP in response and response[TCP].flags == 0x12:
            rst_packet = IP(dst=ip) / TCP(dport=port, flags="R")
            sr1(rst_packet, timeout=1, verbose=0)
            return True
    except Exception as e:
        return False
    return False

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        if scan_port(ip, port):
            open_ports.append(port)
    return open_ports

def worker(ip, ports, result_queue):
    open_ports = scan_ports(ip, ports)
    result_queue.put((ip, open_ports))

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

#Citādi windowsā var sanākt, ka prasa vairākas reizes ievadīt ip adresi
def main():
    
    ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 3306, 3389, 8080]   

    ips = input("Ievadi IP adreses, atdalot ar komatu: ").split(",") #izvācama komatus
    ips = [ip.strip() for ip in ips] #izvācam atstarpes

    valid_ips = [ip for ip in ips if validate_ip(ip)] #izvācam nederīgās IP adreses
    invalid_ips = [ip for ip in ips if not validate_ip(ip)] #izvācam nederīgās IP adreses

    if invalid_ips:
        print(f"Šīs IP adreses ir nederīgas un netiks skenētas: {', '.join(invalid_ips)}")
        
    result_queue = multiprocessing.Queue()
    processes = []

    print(f"Skenēju portus {ports}...")
    try:
        for ip in valid_ips:
                process = multiprocessing.Process(target=worker, args=(ip, ports, result_queue))
                processes.append(process)
                process.start()

        for process in processes:
                process.join()

        while not result_queue.empty():
                ip, open_ports = result_queue.get()
                print(f"IP adresei {ip} ir atvērti {open_ports} porti.")
    except Exception as e:
        print("Kļūda:", e)            

#Lai main izpildītu tikai vienu reizi
if __name__ == "__main__":
    main()
 