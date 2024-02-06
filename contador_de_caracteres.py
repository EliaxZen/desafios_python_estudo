# Crie um código que conta o número de vogais de um bloco de texto qualquer. O código deve desconsiderar letras
# maiúsculas/minúsculas, isto é, "a" e "A" contam da mesma forma.
# O texto pode ser colocado diretamente como um string no cógigo.

texto = """Python é uma linguagem de programação de alto nível,[5] interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.[1] Atualmente, possui um modelo de
desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation.
Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo,
não é formalmente especificada. O padrão na pratica é a implementação CPython."""


letraA = texto.count("a") + texto.count("A")
letraE = texto.count("e") + texto.count("E")
letraI = texto.count("i") + texto.count("I")
letraO = texto.count("o") + texto.count("O")
letraU = texto.count("u") + texto.count("U")

print(f"Há {letraA} letras A no texto!")
print(f"Há {letraE} letras E no texto!")
print(f"Há {letraI} letras I no texto!")
print(f"Há {letraO} letras O no texto!")
print(f"Há {letraU} letras U no texto!")