import math
a = int(input('Informe um valor pra a: '))
b = int(input('Informe um valor pra b: '))
c = int(input('Informe um valor pra c: '))
print(f'A equação é {a}x² + {b}x + c = 0')
delta = b ** 2 - 4 * a * c
if delta < 0:
    print('Não existe raiz')
elif delta == 0:
    raiz = (-1 * b + (math.sqrt(delta)) / 2 * a)
    print(raiz)
elif delta >= 0:
    print('Existem duas raizes reais')
    raiz1 = (-1 * b + (math.sqrt(delta)) / 2 * a)
    raiz2 = (-1 * b - (math.sqrt(delta)) / 2 * a)
    print(f'x1 = {raiz1}')
    print(f'x2 = {raiz2}')
