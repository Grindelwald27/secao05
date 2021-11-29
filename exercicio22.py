idade = int(input('Informe sua idade: '))
tempo_trabalhado = int(input('Informe seu tempo de serviço em anos: '))
if idade >= 65:
    print('Você pode se aposentar!')
elif idade < 65 and tempo_trabalhado >= 30:
    print('Você pode se aposentar!')
elif idade >= 60 and tempo_trabalhado >= 25:
    print('Você pode se aposentar!')
else:
    print('Você ainda não pode se aposentar')
