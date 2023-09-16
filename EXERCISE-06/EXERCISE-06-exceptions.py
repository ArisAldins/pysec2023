def exception_example(value):
    try:
        if value < 0:
            raise ValueError("Vērtība nedrīkst būt nenegatīva.")
        result = 10 / value  # dalīšana
        item = [1, 2, 3]
        element = item[value]  # pieeja list elementam
        print(f"Rezultāts: {result}, Elements: {element}")
    except ZeroDivisionError:
        print("Kļūda: Tiek dalīts ar 0")
    except TypeError:
        print("Kļūda: Nepareizs tips")
    except ValueError as ve:
        print(f"Nepareiza vērtība: {ve}")
    except IndexError:
        print("Kļūda: Indekss ārpus diapazona")
    except Exception as e:
        print(f"Radās negaidīts izņēmums: {e}")
    else:
        print("Nav izņēmumu.")
    finally:
        print("Izpilde pabeigta")

# testē dažādus izņēmumu piemērus
exception_example(5)  # nav izņēmums
exception_example(-2)  # nepareiza vērtība
exception_example(0)  # dala ar 0
exception_example(2)  # indeksa kļūda


