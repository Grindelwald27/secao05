altura = float(input('Informe sua altura: '))
sexo = input('Informe o sexo m/f: ')
if sexo == 'm':
    peso_ideal_m = (72.7 * altura) - 58
    print('Seu peso ideal é %.2f kg' % peso_ideal_m)
elif sexo == 'f':
    peso_ideal_f = (62.1 * altura) - 44.7
    print('Seu peso ideal é %.2f kg' % peso_ideal_f)
else:
    print('Gênero não identificado')
