ano = int(input('Informe um ano e descubra se ele é um ano bissexto: '))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')
