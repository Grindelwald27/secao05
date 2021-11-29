x = int(input('Informe o primeiro número: '))
y = int(input('Informe o segundo número: '))
z = int(input('Informe o terceiro número: '))
print('Escolha uma das opções para calcular a média')
print('a - Geométrica')
print('b - Ponderada')
print('c - Harmônica')
print('d - Aritmética')
op = input('Opção: ')
if op == 'a':
    geometrica = (x * y * z) ** 1 / 3
    print(geometrica)
elif op == 'b':
    ponderada = (x + 2 * y + 3 * z) / 6
    print(ponderada)
elif op == 'c':
    harmonica = 1 / (1 / x + 1 / y + 1 / z)
    print(harmonica)
elif op == 'd':
    aritmetica = (x + y + z) / 3
    print(aritmetica)
