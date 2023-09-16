#EXERCISE 3
#DATU TIPU DEMONSTRĀCIJA

# Izveido listi ar pilsētām
cities_list = ["Valmiera", "Cesis", "Riga", "Daugavpils"]

# Piekļūst elementiem listē
first_two_cities = cities_list[:2]  # piekļūst pirmajiem diviem
last_two_cities = cities_list[-2:]  # piekļūst pēdējiem diviem

# Modificē listi pieliekot papildus listi
additional_cities = ["Rezekne", "Talsi"]
cities_list.extend(additional_cities)

# Printē modificēto pilsētu listi
print("Pilsētu liste:", cities_list)

# Izveido vārdnīcu ar info par grāmatām
book_info = {
    "title": "Mērnieku laikie",
    "author": "Kaudzītess",
    "year": 1879,
}

# piekļūst vērtībai vārdnīcā
book_title = book_info["title"]  


# Modificē vērtību vārdnīcā
book_info["year"] = 2023

# Izprintē modificēto vārdnīcu
print("Info par grāmatām:", book_info)

# Izveido setu ar mašīnām
car_set = {"Ford", "Tesla", "MB", "GAZ"}

# Pārbauda vai elements ir setā (nav)
has_Volvo = "Volvo" in car_set  

# Izņem elementu no seta
car_set.discard("GAZ")

# Izprintē modificēto setu
print("Mašīnas:", car_set)

# Izveido tupli mašīnai
car1 = ("VAZ", "2115", 1985, "Mitrs asfalts", 100000)

# Ar indeksiem piekļūst elementiem
make = car1[0]         # marka
model = car1[1]        # modelis
year = car1[2]         # gads
color = car1[3]        # krāsa
price = car1[4]        # cena

# Izprintē info par mašīnu
print("Info par mašīnu:")
print(f"Marka: {make}")
print(f"Modelis: {model}")
print(f"Gads: {year}")
print(f"Krāsa: {color}")
print(f"Cena: ${price}")
