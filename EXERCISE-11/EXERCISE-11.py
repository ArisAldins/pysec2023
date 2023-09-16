import signal
import time

# definē indikatoru 
exit_gracefully = False

# definē signāla hendleri funkcijai priekš Ctrl+C
def signal_handler(sig, frame):
    global exit_gracefully
    print("\nCtrl+C ir nospiests. Eleganti beidzam programmu...:) ) ")
    exit_gracefully = True

# reģistrē Ctrl+C signāla hendleri
signal.signal(signal.SIGINT, signal_handler)

# uzdevumi 1-1000
def long_running_task():
    for i in range(1, 1000):
        if exit_gracefully:
            break
        print(f"Uzdevums {i}")
        time.sleep(1)

# izpilda uzdevumus
try:
    long_running_task()
except KeyboardInterrupt:
    pass

print("Programmas izpilde ir pabeigta.")
