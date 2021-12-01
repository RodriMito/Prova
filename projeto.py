horaE = int(input("Coloque a hora da entrada: \n"))
minutoE = int(input("Coloque os minutos da entrada: \n"))
horaS = int(input("Coloque a hora da saída: \n"))
minutoS = int(input("Coloque os minutos da saída: \n"))

if horaE > horaS:
    hora_final = (horaS + 24) - horaE
else:
    hora_final = horaS - horaE

if minutoE > minutoS:
    minuto_final = (minutoS + 60) - minutoE
else:
    minuto_final = minutoS - minutoE

print(f"A permanência foi de: {hora_final} horas e {minuto_final} minutos \n")

tempo_minutos = hora_final * 60 + minuto_final

if 1 <= tempo_minutos <= 60:
    preco = 1
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 60 < tempo_minutos <= 120:
    preco = 2
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 120 < tempo_minutos <= 180:
    preco = 4.2
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 180 < tempo_minutos <= 240:
    preco = 5.6
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif tempo_minutos > 240:
    preco = hora_final * 2
    print(f"O valor a ser pago será de R$ {float(preco)}")
else:
    print(f"Tempo de permanência mínimo, não será necessário pagar!")
