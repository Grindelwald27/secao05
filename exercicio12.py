import math

num = int(input('Informe um valor: \n'))
if num < 0:
    print('Número inválido')
else:
    print(f'{math.log(num)}')
