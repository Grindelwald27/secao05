chegada = str(input('Informe o horário de chegada hh:mm: '))
saida = str(input('Informe o horário de saída hh:mm: '))
hora, minuto = chegada.split(':')
horaS, minutoS = saida.split(':')
hora = int(hora)
minuto = int(minuto)
horaS = int(horaS)
minutoS = int(minutoS)
tempoM = 0
tempoH = 0
if hora < horaS:
    tempoH = (horaS - hora)
    if minuto < minutoS:
        tempoH = tempoH + 1
elif hora > horaS:
    tempoH = 24 - (hora - horaS)
    if minuto < minutoS:
        tempoH = tempoH + 1
elif hora == horaS and minuto > minutoS:
    tempoH = 24
elif hora == horaS and minuto == minutoS:
    tempoH = 1
elif hora == horaS and minuto < minutoS:
    tempoH = 1
if tempoH < 3:
    print(f'O valor cobrado será de R${tempoH * 1:.2f}')
elif 2 < tempoH < 5:
    print(f'O valor cobrado será de R${(2 * 1) + ((tempoH - 2) * 1.4):.2f}')
else:
    print(f'O valor cobrado será de R${((2 * 1) + (2 * 1.4)) + ((tempoH - 4) * 2):.2f}')
