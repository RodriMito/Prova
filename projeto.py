h_entrada = int(input("Digite a hora de entrada \n"))
m_entrada = int(input("Digite os minutos de entrada \n"))
h_saida = int(input("Digite a hora de saída \n"))
m_saida = int(input("Digite os minutos de saída \n"))

if h_entrada > h_saida:
    hora_final = (h_saida + 24) - h_entrada
else:
    hora_final = h_saida - h_entrada

if m_entrada > m_saida:
    minuto_final = (m_saida + 60) - m_entrada
else:
    minuto_final = m_saida - m_entrada

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