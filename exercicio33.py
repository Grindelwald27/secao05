preco_antigo = int(input('Informe o preço: '))
aumento1 = (preco_antigo * 5) / 100
aumento2 = (preco_antigo * 10) / 100
aumento3 = (preco_antigo * 15) / 100
pn1 = preco_antigo + aumento1
pn2 = preco_antigo + aumento2
pn3 = preco_antigo + aumento3
if preco_antigo <= 50:
    print(f'O novo preço é R${aumento1 + preco_antigo}')
elif 50 < preco_antigo < 100:
    print(f'O novo preço é R${aumento2 + preco_antigo}')
elif preco_antigo > 100:
    print(f'O novo preço é R${aumento3 + preco_antigo}')
if pn1 < 80 or pn2 < 80 or pn3 < 80:
    print('Barato')
elif 80 <= pn1 <= 120 or 80 <= pn2 <= 120 or 80 <= pn3 <= 120:
    print('Normal')
elif 120 <= pn1 <= 200 or 120 <= pn2 <= 200 or 120 <= pn3 <= 200:
    print('Caro')
elif pn1 > 200 or pn2 > 200 or pn3 > 200:
    print('Muito caro')
