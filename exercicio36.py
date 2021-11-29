venda_mensal = int(input('Informe o valor da venda mensal: R$'))
if venda_mensal >= 100_000.00:
    comissao = 700.00 + (venda_mensal * 16) / 100
    print(f'A comissão é R${comissao}')
elif 80_000.00 <= venda_mensal < 100_000.00:
    comissao = 650.00 + (venda_mensal * 14) / 100
    print(f'A comissão é R${comissao}')
elif 60_000.00 <= venda_mensal < 80_000.00:
    comissao = 600.00 + (venda_mensal * 14) / 100
    print(f'A comissão é R${comissao}')
elif 40_00.00 <= venda_mensal < 60_000.00:
    comissao = 550.00 + (venda_mensal * 14) / 100
    print(f'A comissão é R${comissao}')
elif 20_000.00 <= venda_mensal < 40_000.00:
    comissao = 500.00 + (venda_mensal * 14) / 100
    print(f'A comissão é R${comissao}')
elif venda_mensal < 20_000.00:
    comissao = 400.00 + (venda_mensal * 14) / 100
    print(f'A comissão é R${comissao}')
