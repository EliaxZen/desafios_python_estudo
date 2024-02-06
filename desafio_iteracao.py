numeros = [1, 10, 7, 2, 11, 23, 10]

soma_dos_numeros = 0
maior_numero = numeros[0]

for n in numeros:
    soma_dos_numeros += n
    media_dos_numeros = soma_dos_numeros / len(numeros)
    
print('----- DESAFIO 1 -----')
print(f'A soma dos números é: {soma_dos_numeros:.2f}')
print(f'A média dos números é: {media_dos_numeros:.2f}')


for m in numeros:
    if m > maior_numero:
        maior_numero = m

print('----- DESAFIO 2 -----')
print(f'O maior número é: {maior_numero}')


palavras = ['Maça', 'Banana', 'Jaca', 'Melão', 'Abacaxi']

print('----- DESAFIO 3 -----')
for p in palavras:
    if len(p) >= 5:
        print(f'Palavra mínimo 5 caracteres: {p}')

    




