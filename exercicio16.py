mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
       'Novembro', 'Dezembro']
num = int(input('Informe um número entre 1 a 12: '))
if 1 < num > 12:
    print('Esse mês não existe')
else:
    print(f'O mês selecionado é {mes[num - 1]}.')
