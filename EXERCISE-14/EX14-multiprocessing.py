# vienkāršs multiprocessing piemērs

import multiprocessing

# funkcija rēķina vērtību kvadrātā
def calculate_square(number):
    result = number * number
    print(f" {number} kvadrātā ir {result}")

if __name__ == "__main__":
    # izveido skaitļu listi
    numbers = [1, 2, 3, 4, 5]

    # izveido procesu kopumu
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # izmanto kopumu, lai pielietotu funkciju uz skaitļiem paralēli
        pool.map(calculate_square, numbers)
