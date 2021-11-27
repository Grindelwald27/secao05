base_maior = int(input('Informe o comprimento da base maior: '))
base_menor = int(input('Informe o comprimento da base menor: '))
altura = int(input('Informe a altura: '))
area = ((base_maior + base_menor) * altura) / 2
if base_menor > 0 and base_maior > 0:
    print(f'A área do trapézio é {area}m²')
else:
    if base_maior < 0:
        print('Informe valor da base maior acima de 0'.format(base_maior))
    if base_menor < 0:
        print('Informe valor da base menor acima de 0'.format(base_menor))
