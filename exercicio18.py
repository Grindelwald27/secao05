print('Escolha uma das opções abaixo')
op = input('soma, subtração, divisão ou multiplicação: ')
if op == 'soma':
    num1 = int(input('Informe um número: '))
    num2 = int(input('Informe outro número: '))
    soma = num1 + num2
    print(soma)
if op == 'subtração':
    num1 = int(input('Informe um número: '))
    num2 = int(input('Informe outro número: '))
    subtracao = num1 - num2
    print(subtracao)
if op == 'divisão':
    num1 = int(input('Informe um número: '))
    num2 = int(input('Informe outro número: '))
    divisao = num1 / num2
    print(divisao)
if op == 'multiplicação':
    num1 = int(input('Informe um número: '))
    num2 = int(input('Informe outro número: '))
    multiplicacao = num1 * num2
    print(multiplicacao)
