import multiprocessing
from scapy.all import *

def scan(target, port):
    # izveido TCP SYN paketi
    syn_packet = IP(dst=target) / TCP(dport=port, flags="S")

    # sūta paketi un gaida atbildi
    response = sr1(syn_packet, timeout=1, verbose=0)

    # pārbauda vai atbilde saņemta
    if response and response.haslayer(TCP):
        # pārbauda vai atbildei ir SYN-ACK karogs
        if response[TCP].flags == 0x12:
            print(f"Ports {port} adresē {target} ir atvērts")

def main():
    target_ip = "latvija.gov.lv" # adrese, kuru skenēs
    ports = range(1, 1025)  # porti, kurus skenēs

    # izveido procesu kopumu
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    # izmanto kopumu, lai skenētu portus paralēli
    results = [pool.apply_async(scan, args=(target_ip, port)) for port in ports]

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
