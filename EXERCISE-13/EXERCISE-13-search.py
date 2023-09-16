# nestrādājošs meklēšanas scripta mēģinājums. EXERCISE-13.py failā realizēta pieslēgšanās FTP no manuāli veidotas serveru listes, bez meklēšanas.

import re
from googlesearch import search
import time

# funkcija ftp serveru googlēšanai
def find_ftp_servers_with_login(query, num_results=20):
    try:
        print(f"Meklē FTP serverus: {query}")
        # izpilda meklēšanu
        search_results = search(query, num_results=num_results)

        # meklē ftp loginus pēc šablona
        ftp_pattern = r'ftp://(.*?):(.*?)@'

        # inicializē listi, kurā glabās serverus
        ftp_servers = []

        # iet cauri meklēšanas rezultātiem
        for idx, result in enumerate(search_results, start=1):
            server_info = {'url': result}

            # iegūst login info
            match = re.search(ftp_pattern, result)
            if match:
                login, password = match.groups()
                server_info['login'] = login
                server_info['password'] = password
            else:
                server_info['login'] = None
                server_info['password'] = None

            ftp_servers.append(server_info)

            # pauze starp pieprasījumiem, lai izvairītos no limitēšanas vai bloķēšanas
            if idx < num_results:
                time.sleep(5)  # pauzes ilgums

        return ftp_servers
    except Exception as e:
        print(f"Meklēšanas laikā radās kļūda: {e}")
        return []

# izsauc funkciju (limitē uz 20 rezultātiem)
ftp_servers = find_ftp_servers_with_login('inurl:ftp -inurl:(http|https)', num_results=20)

# izvada ftp serverus un loginus
for idx, server in enumerate(ftp_servers, start=1):
    print(f"{idx}. URL: {server['url']}")
    if server['login'] is not None:  
        print(f"   Lietotājs: {server['login']}")
        print(f"   Parole: {server['password']}")
    else:
        print("   Nav atrastas login detaļas")
    print()

