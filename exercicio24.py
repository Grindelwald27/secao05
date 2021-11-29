valor = float(input('Informe o valor do produto: '))
print('Escolha o Estado de destino')
print('1 - Minas Gerais')
print('2 - São Paulo')
print('3 - Rio de Janeiro')
print('4 - Mato Grosso do Sul')
op = int(input('Opção: '))

while op < 1 or op > 4:
    print('Erro! Informe uma opção válida')
    print('1 - Minas Gerais')
    print('2 - São Paulo')
    print('3 - Rio de Janeiro')
    print('4 - Mato Grosso do Sul')
    op = int(input('Opção: '))

if op == 1:
    print(f'O valor total é R${valor + (valor * 7) / 100}')
elif op == 2:
    print(f'O valor total é R${valor + (valor * 12) / 100}')
elif op == 3:
    print(f'O valor total é R${valor + (valor * 15) / 100}')
elif op == 4:
    print(f'O valor total é R${valor + (valor * 8) / 100}')
