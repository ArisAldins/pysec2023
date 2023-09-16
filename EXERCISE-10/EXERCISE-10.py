# programma vāc virsrakstus no ziņu lapām

import threading
import requests
from bs4 import BeautifulSoup
import time

# definē vietnes, no kurām vāks datus
news_websites = [
    'https://www.delfi.lv',
    'https://www.tvnet.lv',
    'https://www.apollo.lv',
]

print_lock = threading.Lock()

# funkcija pirmo 10 virsrakstu savākšanai no vietnēm + izmēra patērēto laiku katrai
def scrape_news_headlines(url):
    start_time = time.time()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            with print_lock:
                print(f"---------- Pirmie 10 virsraksti no {url}: -----------")
                # limitē virsrakstus līdz 10
                for i, headline in enumerate(headlines):
                    if i >= 10:
                        break
                    print(headline.text.strip())
                print(f"--- Laiks datu savākšanai no {url}: {time.time() - start_time:.2f} sekundes\n")
    except Exception as e:
        with print_lock:
            print(f"Kļūda vācot datus {url}: {e}")

# izveido un palaiž pavedienu katrai vietnei
threads = []
for website in news_websites:
    thread = threading.Thread(target=scrape_news_headlines, args=(website,))
    threads.append(thread)
    thread.start()

# gaida līdz visi pavedieni beigs darbu
for thread in threads:
    thread.join()

print("Visi pavedieni ir beiguši vākt datus!")
