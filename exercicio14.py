nota_laboratorio = int(input('Informe sua nota de laboratório: '))
nota_av_semestral = int(input('Informe sua nota da avaliação semestral: '))
nota_ex_final = int(input('Informe a nota do exame final: '))
media = ((nota_laboratorio * 2) + (nota_av_semestral * 3) + (nota_ex_final * 5)) / (2 + 3 + 5)
print(media)
if 0 < media <= 2.9:
    print('Reprovado!')
elif 3.0 < media <= 4.9:
    print('Recuperação')
elif media > 5:
    print('Aprovado')
