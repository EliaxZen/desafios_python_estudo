# Combasenofor loopabaixo:
valores = [1, 2, 3, 5, 10]

quadrados_maiores_que_tres = []
for valor in valores:
    if valor > 3:
        quadrado = valor ** 2
        quadrados_maiores_que_tres.append(quadrado)

print(quadrados_maiores_que_tres)
# output: [25, 100]

# Crie uma compreensão de lista que gera a mesma lista quadrados_maiores_que_tres. Em
# seguida, use as funções map e filter para fazer a mesma coisa.

quadrados_maiores_que_tres = [
    valor ** 2
    for valor in valores
    if valor > 3
]

quadrados_maiores_que_tres = list(map(lambda x: x ** 2, filter(lambda x: x > 3, valores)))

print(quadrados_maiores_que_tres)
