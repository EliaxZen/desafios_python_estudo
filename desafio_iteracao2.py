# Dado duas listas, printe todos os valores que aparecerem duplicados nas duas listas

# Dado duas listas, printe uma mensagem dizendo se existe algum elemento em comum entre elas ou não.

lista1 = ['Maçã', 'Uva', 'Abacaxi', 'Jaca', 'Melancia']
lista2 = ['Melao', 'Uva', 'Abacaxi', 'Melancia']

valores_duplicados = 0

print('----- DESAFIO 1 -----')

for valor1 in lista1:
    for valor2 in lista2:
        if valor1 == valor2:
            print(f'* {valor1} * aparece nas duas listas')

print('----- DESAFIO 2 -----')

lista3 = ['Pedro', 475, True]
lista4 = ['Pedro', 45, False]

itens_em_comum = False

for x in lista3:
    for y in lista4:
        if x == y:
            itens_em_comum = True
            break

if itens_em_comum:
    print(f'Item duplicado na lista: {itens_em_comum}')
else:
    print(f'Item duplicado na lista: {itens_em_comum}')