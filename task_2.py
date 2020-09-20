def temp_calc():
    temp_value = int(input('Enter the value:\n'))
    temp_type = input('Enter the type:\n')
    if temp_type == 'C':
        k = temp_value - 273.15
        c = temp_value
        f = int((temp_value + 459.67) / 1.8)
        print(f'Kelvins {k},Celsius {c}, Fahrenheits {f}')
    elif temp_type == 'K':
        c = temp_value + 273.15
        k = temp_value
        f = int(temp_value - 32) / 1.8
        print(f'The temperature in Kelvins is {k}, in Celsius is {c}, in Fahrenheits is {f}')
    elif temp_type == 'F':
        f = temp_value
        k = int((temp_value + 459.67) / 1.8)
        c = int((temp_value - 32) / 1.8)
        print(f'The temperature in Kelvins is {k}, in Celsius is {c}, in Fahrenheits is {f}')

temp_calc()


