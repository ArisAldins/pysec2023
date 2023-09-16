# izmanto computer_operations.py moduli

import computer_operations

my_computer = {"Ražotājs": "Apple", "Modelis": "MacBook Pro M2", "OS": "MacOS Ventura"}

computer_operations.power_on(my_computer)
computer_operations.reboot(my_computer)
computer_operations.shut_down(my_computer)

# izmanto computer_info.py moduli
import computer_info

computer_info_str = computer_info.get_computer_info(my_computer)
print(computer_info_str)
