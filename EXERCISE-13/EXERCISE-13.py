# programma no manuāli veidotas ftp listes ielogojas un atgriež serveru root dir saturu.

# ftp meklēšanu, lai veidotu listi automātiski no rezultātiem neizdevās realizēt.
# nelikās arī ļoti loģiski, kāpēc googlē būtu jāmētājas publiskiem ftp serveriem ar loginiem (???), 
# lai gan šie 3 listē tādi ir.

# meklēšanu mēģināju realizēt gan ar pygoogle, gan googlesearch - bet izskatās, ka loginiem būtu jāglabājas
# specifiskā un vienādā formātā, lai tos varētu atrast, atpazīt un savākt (???).

# EXERCISE-13-search.py failā ir atsevišķi meklēšanas koda mēģinājums, kas nestrādā.


import ftplib
import threading
import queue

# manuāli veidota ftp serveru liste
ftp_servers = [
    {
        'host': 'ftp.mirror.rafal.ca',
        'username': 'ftp',
        'password': 'email@example.com',
    },
    {
        'host': 'ftp.scene.org',
        'username': 'ftp',
        'password': 'email@example.com',
    },
    {
        'host': 'ftp.rebex.net',
        'username': 'demo',
        'password': 'password',
    }
]

# funkcija, kas listē root dir
def list_root_directory(ftp_server, results_queue):
    try:
        # pieslēdzas ftp serverim
        ftp = ftplib.FTP(ftp_server['host'])
        ftp.login(user=ftp_server['username'], passwd=ftp_server['password'])

        # listē root dir
        root_dir_contents = ftp.nlst()
        header_line = f"----- Root dir saturs no servera {ftp_server['host']}: -----"
        results_queue.put(header_line)

        for item in root_dir_contents:
            if '/' not in item:
                results_queue.put(f"{ftp_server['host']} - {item}")

        # izlogojas un slēdz savienojumu
        ftp.quit()
    except Exception as e:
        results_queue.put(f"Error while processing {ftp_server['host']}: {e}")

# funkcija, kas apstrādā ftp serverus izmantojot pavedienus
def process_ftp_servers(ftp_servers):
    # izveido rindu, kur glabāt rezultātus
    results_queue = queue.Queue()

    # izveido worker threads
    threads = []
    for server_config in ftp_servers:
        thread = threading.Thread(target=list_root_directory, args=(server_config, results_queue))
        threads.append(thread)

    # palaiž worker threads
    for thread in threads:
        thread.start()

    # gaida kad visi pavedieni izpildīsies
    for thread in threads:
        thread.join()

    # apstrādā un izvada rezultātus no rindas
    while not results_queue.empty():
        result = results_queue.get()
        print(result)

# izsauc funkciju, kas apstrādā ftp serverus
process_ftp_servers(ftp_servers)
