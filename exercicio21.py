print('Escolha uma das opções')
print('1 - Soma de 2 números.')
print('2 - Diferença entre 2 números.')
print('3 - Produto entre 2 números.')
print('4 - Divisão entre 2 números')
escolha = int(input('Opção: '))
if escolha == 1:
    num1 = int(input('Informe um número: '))
    num2 = int(input('Informe outro número: '))
    soma = num1 + num2
    print(soma)
elif escolha == 2:
    num1 = int(input('Informe um número: '))
    num2 = int(input('Informe outro número: '))
    if num1 > num2:
        diferenca = num1 - num2
        print(diferenca)
    else:
        diferenca = num2 - num1
        print(diferenca)
elif escolha == 3:
    num1 = int(input('Informe um número: '))
    num2 = int(input('Informe outro número: '))
    multiplicacao = num1 * num2
    print(multiplicacao)
elif escolha == 4:
    num1 = int(input('Informe um número: '))
    num2 = int(input('Informe outro número: '))
    while num2 == 0:
        print('O denominador não pode ser zero')
        num1 = int(input('Informe um número: '))
        num2 = int(input('Informe outro número: '))
    divisao = num1 / num2
    print(divisao)
else:
    print('Erro! Opção inválida')
