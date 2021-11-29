nota = float(input('Informe a nota: '))
falta = int(input('Informe a quantidade de faltas'))
if 9.0 <= nota <= 10.0:
    if falta <= 20:
        print('A')
    elif falta > 20:
        print('B')
if 7.5 <= nota <= 8.9:
    if falta <= 20:
        print('B')
    elif falta > 20:
        print('C')
if 5.0 <= nota <= 7.4:
    if falta <= 20:
        print('C')
    elif falta > 20:
        print('D')
if 4.0 <= nota <= 4.9:
    if falta <= 20:
        print('D')
    elif falta > 20:
        print('E')
if 0.0 <= nota <= 3.9:
    if falta <= 20:
        print('E')
    elif falta > 20:
        print('E')
