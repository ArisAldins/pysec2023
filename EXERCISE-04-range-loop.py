# mašīnu ātrumi
car_speeds = [60, 70, 80, 90, 100, 120, 200]

# atļautais ātrums pret ko pārbauda
speed_limit = 90

# pārbauda ātrumus pret atļauto
for speed in car_speeds:
    if speed > speed_limit:
        print(f"Auto ātrums {speed} km/h pārsniedz atļauto.")
       
else:
    print("Visi auto brauc ar atļauto ātrumu.")


