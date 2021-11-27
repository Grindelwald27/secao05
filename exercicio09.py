salario = 1000
prestacao = int(input('Informe a parcela da prestação: '))
if prestacao > (salario * 20) / 100:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
