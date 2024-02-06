valores = list(range(10))

maiores_que_cinco = []
for valor in valores:
    if valor > 5:
        maiores_que_cinco.append(valor)

maiores_que_cinco = [
    valor + 10 #RESULTADO
    for valor in valores #para cada ELEMENTO in SEQUÊNCIA
    if valor > 5 #se CONDIÇÃO
]

print(valores)
print(maiores_que_cinco)