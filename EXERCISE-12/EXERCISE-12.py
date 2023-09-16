# uzstāda tqdm lai varētu uztaisīt progress baru 
# C:\python>pip install tqdm

import urllib.request
from tqdm import tqdm  # importē tqdm

# URL failam, kuru lādēs
file_url = 'https://ubuntu.koyanet.lv/releases/22.04.3/ubuntu-22.04.3-desktop-amd64.iso'  # izmantojam publisku ubuntu install .iso failu

# funkcija faila ielādei ar progress baru
def download_file_with_progress(url, local_filename):
    # definē funkciju progress bara atjaunošanai
    def progress_bar_hook(t):
        last_b = [0]
        def update_to(b=1, bsize=1, tsize=None):
            if tsize is not None:
                t.total = tsize
            t.update((b - last_b[0]) * bsize)
            last_b[0] = b
        return update_to

    # lādē failu un rāda progressu
    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=local_filename) as t:
        urllib.request.urlretrieve(url, filename=local_filename, reporthook=progress_bar_hook(t))

# definē ar kādu nosaukumu glabās failu lokāli
local_filename = 'resns_failinjsh.iso'  

download_file_with_progress(file_url, local_filename)

print(f"BOOOM! Fails {local_filename} ir ielādēts veiksmīgi.")
