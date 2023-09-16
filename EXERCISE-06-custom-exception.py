#custom izņēmums, kas pārbauda vai vērtība nav pārāk augsta

class ValueTooHighError(Exception):
    def __init__(self, value, max_value):
        super().__init__(f"Vērtība {value} ir pārāk augsta. Maksimālā pieļaujamā vērtība ir {max_value}.")
        self.value = value
        self.max_value = max_value

def check_value(value, max_value):
    if value > max_value:
        raise ValueTooHighError(value, max_value)
    return value

try:
    max_allowed_value = 100
    value_to_check = 150  # pārāk augsta vērtība
    checked_value = check_value(value_to_check, max_allowed_value)
except ValueTooHighError as e:
    print(f"Kļūda: {e}")
else:
    print(f"Vērtība {checked_value} iekļaujas atļautajā diapazonā.")
