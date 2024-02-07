texto = str(input('Digite um texto para ser cifrado: \n-->'))
chave = int(input("Digite uma chave: \n-->"))

maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"

cifra = ""


def cifrar_caractere(caractere, seq, chave):
    indice_atual = seq.index(caractere)
    novo_indice = indice_atual + chave
    # Lidar com situação onde indice está a direita da sequência
    while novo_indice >= len(seq):
        novo_indice = novo_indice - len(seq)
    # Lidar com situação onde indice está a esquerda da sequência
    while novo_indice < 0:
        novo_indice = novo_indice + len(seq)
    return seq[novo_indice]


for caractere in texto:
    if caractere in minusculas:
        caractere_cifra = cifrar_caractere(caractere, minusculas, chave)
    elif caractere in maiusculas:
        caractere_cifra = cifrar_caractere(caractere, maiusculas, chave)
    else:
        caractere_cifra = caractere
    cifra += caractere_cifra

print(cifra)