altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
if altura < 1.20:
    if peso <= 60:
        print('A')
    elif 60 <= peso <= 90:
        print('D')
    elif peso > 90:
        print('G')
if 1.20 <= altura <= 1.70:
    if peso <= 60:
        print('B')
    elif 60 <= peso <= 90:
        print('E')
    elif peso > 90:
        print('H')
if altura > 1.70:
    if peso <= 60:
        print('C')
    elif 60 <= peso <= 90:
        print('F')
    elif peso > 90:
        print('I')
