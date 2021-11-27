nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    print(f'A média é {media}')
else:
    print('Nota inválida')
