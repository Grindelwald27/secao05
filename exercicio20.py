a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))
c = int(input('Informe o valor de c: '))
while a > c + b:
    print('O valor de "a" não pode ser maior que o valor de "b + c"')
    a = int(input('Informe o valor de a: '))
    b = int(input('Informe o valor de b: '))
    c = int(input('Informe o valor de c: '))
while b > c + a:
    print('O valor de "b" não pode sr maior que o valor de "a + c"')
    a = int(input('Informe o valor de a: '))
    b = int(input('Informe o valor de b: '))
    c = int(input('Informe o valor de c: '))
while c > a + b:
    print('O valor de "c" não pode ser maior que o valor de "a + b"')
    a = int(input('Informe o valor de a: '))
    b = int(input('Informe o valor de b: '))
    c = int(input('Informe o valor de c: '))

if a == b == c:
    print('O triângulo é equilátero')
elif a != b == c or a == b != c or a == c != b:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')
