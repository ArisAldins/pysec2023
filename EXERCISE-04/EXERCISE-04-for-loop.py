cars = ["Ford", "MB", "GAZ", "Tesla", "VAZ"]

for car in cars:
    if car == "VAZ":
        print("Mēs atradām VAZ :) !!!")
        break  # iziet, ja atrasts VAZ
else:
    print("Diemžēl neatradām VAZ :( ") #paziņojums, ja nav atrasts VAZ
