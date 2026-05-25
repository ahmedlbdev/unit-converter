from colorama import Fore

def menu():
    print('Bienvenido al convertidor de unidades. Introduce el numero y la unidad de origen y la que quieres convertir.')
    number = input('Introduce el numero: ')
    from_unit_pre = input('Introduce la unidad de origen: (cm, m, km, in, ft, yd) / (byte, kb, mb, gb):')
    to_unit_pre = input('Introduce la unidad a convertir: (cm, m, km, in, ft, yd) / (byte, kb, mb, gb):')

    from_unit = from_unit_pre.lower()
    to_unit = to_unit_pre.lower()

    units = {
        'cm': 0.01,
        'm': 1,
        'km': 1000,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'byte': 1,
        'kb': 1024,
        'mb': 1024**2,
        'gb': 1024**3
    }
    if from_unit in units and to_unit in units:
        converted_value = float(number) * (units[from_unit] / units[to_unit])
        print(f'{number} {from_unit} son {converted_value} {to_unit}')
    else:
        print(Fore.RED + 'Unidad no reconocida. Por favor, introduce una unidad válida.' + Fore.RESET)
if __name__ == "__main__":
    menu()