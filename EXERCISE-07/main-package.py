# izmanto computers_package pakotni

from computers_package import computer_operations, computer_info

my_computer = {"Ražotājs": "Apple", "Modelis": "MacBook Pro M2", "OS": "MacOS Ventura"}

computer_operations.power_on(my_computer)
computer_operations.reboot(my_computer)

computer_info_str = computer_info.get_computer_info(my_computer)
print(computer_info_str)
