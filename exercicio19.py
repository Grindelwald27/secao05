num = int(input('Informe um número: '))
while num % 3 == 0 and num % 5 == 0:
    num = int(input('Informe outro número: '))
while num % 3 != 0 and num % 5 != 0:
    num = int(input('Informe outro número: '))
if num % 3 == 0:
    print('Esse número é divisível por 3.')
if num % 5 == 0:
    print('Esse número é divisível por 5.')
