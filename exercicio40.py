custo_fabrica = float(input('Informe o custo de fábrica: '))
if custo_fabrica < 12_000.00:
    distribuidor = (custo_fabrica * 5) / 100
    impostos = 0
    custo_consumidor = custo_fabrica + distribuidor + impostos
    print(f'O valor do carro é R${custo_consumidor}')
elif 12_000.00 <= custo_fabrica <= 25_000.00:
    distribuidor = (custo_fabrica * 10) / 100
    impostos = (custo_fabrica * 15) / 100
    custo_consumidor = custo_fabrica + distribuidor + impostos
    print(f'O valor do carro é R${custo_consumidor}')
elif custo_fabrica > 25_000.00:
    distribuidor = (custo_fabrica * 15) / 100
    impostos = (custo_fabrica * 20) / 100
    custo_consumidor = custo_fabrica + distribuidor + impostos
    print(f'O valor do carro é R${custo_consumidor}')
