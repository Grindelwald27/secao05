salario_atual = float(input('Informe seu salário atual: R$'))
tempo_servico = int(input('Informe o tempo de serviço: '))
if salario_atual <= 500.00:
    if tempo_servico < 1:
        bonus = 0
        reajuste = salario_atual + (salario_atual * 25) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
        print('Você não possui nenhum bônus')
    elif 1 <= tempo_servico <= 3:
        bonus = 100.00
        reajuste = salario_atual + (salario_atual * 25) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif 4 <= tempo_servico <= 6:
        bonus = 200.00
        reajuste = salario_atual + (salario_atual * 25) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif 7 <= tempo_servico <= 10:
        bonus = 300.00
        reajuste = salario_atual + (salario_atual * 25) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif tempo_servico > 10:
        bonus = 500
        reajuste = salario_atual + (salario_atual * 25) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
elif salario_atual <= 1000.00:
    if tempo_servico < 1:
        bonus = 0
        reajuste = salario_atual + (salario_atual * 20) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
        print('Você não possui nenhum bônus')
    elif 1 <= tempo_servico <= 3:
        bonus = 100.00
        reajuste = salario_atual + (salario_atual * 20) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif 4 <= tempo_servico <= 6:
        bonus = 200.00
        reajuste = salario_atual + (salario_atual * 20) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif 7 <= tempo_servico <= 10:
        bonus = 300.00
        reajuste = salario_atual + (salario_atual * 20) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif tempo_servico > 10:
        bonus = 500
        reajuste = salario_atual + (salario_atual * 20) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
elif salario_atual <= 1500.00:
    if tempo_servico < 1:
        bonus = 0
        reajuste = salario_atual + (salario_atual * 15) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
        print('Você não possui nenhum bônus')
    elif 1 <= tempo_servico <= 3:
        bonus = 100.00
        reajuste = salario_atual + (salario_atual * 15) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif 4 <= tempo_servico <= 6:
        bonus = 200.00
        reajuste = salario_atual + (salario_atual * 15) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif 7 <= tempo_servico <= 10:
        bonus = 300.00
        reajuste = salario_atual + (salario_atual * 15) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif tempo_servico > 10:
        bonus = 500
        reajuste = salario_atual + (salario_atual * 15) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
elif salario_atual <= 2000.00:
    if tempo_servico < 1:
        bonus = 0
        reajuste = salario_atual + (salario_atual * 10) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
        print('Você não possui nenhum bônus')
    elif 1 <= tempo_servico <= 3:
        bonus = 100.00
        reajuste = salario_atual + (salario_atual * 10) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif 4 <= tempo_servico <= 6:
        bonus = 200.00
        reajuste = salario_atual + (salario_atual * 10) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif 7 <= tempo_servico <= 10:
        bonus = 300.00
        reajuste = salario_atual + (salario_atual * 10) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif tempo_servico > 10:
        bonus = 500
        reajuste = salario_atual + (salario_atual * 10) / 100 + bonus
        print(f'Seu salário agora é de R${reajuste}')
elif salario_atual > 2000:
    if tempo_servico < 1:
        bonus = 0
        print(f'Seu salário agora é de R${salario_atual}')
        print('Você não possui nenhum bônus')
    elif 1 <= tempo_servico <= 3:
        bonus = 100.00
        reajuste = salario_atual + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif 4 <= tempo_servico <= 6:
        bonus = 200.00
        reajuste = salario_atual + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif 7 <= tempo_servico <= 10:
        bonus = 300.00
        reajuste = salario_atual + bonus
        print(f'Seu salário agora é de R${reajuste}')
    elif tempo_servico > 10:
        bonus = 500
        reajuste = salario_atual + bonus
        print(f'Seu salário agora é de R${reajuste}')
