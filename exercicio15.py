dia_semana = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']
num = int(input('Informe um número entre 1 e 7: '))
if 1 < num > 7:
    print('Esse dia não existe')
else:
    print(f'O dia selecionado é {dia_semana[num - 1]}.')
