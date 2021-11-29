altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.6 <= imc <= 24.9:
    print('Saudável')
elif 25.0 <= imc <= 29.9:
    print('Peso em excesso')
elif 30.0 <= imc <= 34.9:
    print('Obesidade Grau I')
elif 35.0 <= imc <= 39.9:
    print('Obesidade Grau II (severa)')
elif imc >= 40.0:
    print('Obesidade Grau III (mórbida)')
