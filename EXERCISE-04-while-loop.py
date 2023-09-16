# autosacensību simulācija

# mašīnu ātrumi un metri līdz finišam
car1_speed = 70
car2_speed = 75
finish_line = 1000  

# mašīnu pozīcijas
car1_position = 0
car2_position = 0

# simulācija
while car1_position < finish_line and car2_position < finish_line:
    car1_position += car1_speed
    car2_position += car2_speed

    print(f"1. mašīna ir pie {car1_position} metriem.")
    print(f"2. mašīna ir pie {car2_position} metriem.")

else:
    if car1_position >= finish_line:
        print("1. mašīna uzvar! WOOHOO!!!")
    elif car2_position >= finish_line:
        print("2. mašīna uzvar! WOOHOO!!!")
