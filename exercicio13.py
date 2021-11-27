nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda nota: '))
nota3 = int(input('Informe a terceira nota: '))
media = ((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / (1 + 1 + 2)
if media > 60:
    print(media)
    print('Você foi aprovado!')
else:
    print(media)
    print('Você foi reprovado')
