#uz Win taisīju tāpēc cita direktorija un random dati
#pievienoju git arī failus, kurus lasīja.

# definē no kurienes lasīs
log_directory = '/Users/Lektors/Desktop/var/log/messages/'

# definē keywordus meklēšanai
usb_keywords = ['usb', 'USB', 'usbcore', 'usbutils', 'usb-storage', 'usbhid', 'usbfs']

import os

# parbauda failus direktorijā
for filename in os.listdir(log_directory):
    if os.path.isfile(os.path.join(log_directory, filename)):
        try:
            with open(os.path.join(log_directory, filename), 'r') as log_file:
                print(f"Logs from file: {filename}")
                for line in log_file:
                    # meklē keywordus
                    if any(keyword in line for keyword in usb_keywords):
                        print(line.strip())  # izvada līnijas, ja atrod keywordus

        except PermissionError:
            print(f"Kļūda: Nav atļauts lasīt failu '{filename}'.")

