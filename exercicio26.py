distancia = float(input('Informe a distância percorrida: '))
litros = float(input('Informe a quantidade de gasolina durante o percurso: '))
consumo = distancia / litros
if consumo < 8:
    print(consumo)
    print('Venda o carro!')
elif 8 <= consumo <= 14:
    print(consumo)
    print('Econômico')
elif consumo > 12:
    print(consumo)
    print('Super econômico!')
