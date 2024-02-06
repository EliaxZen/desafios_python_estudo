capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas",
}

print("---------- JOGO DAS CAPITAIS ----------")

continuar = True

respostas = 0

acertos = 0


for estado, capital in capitais.items():

    if not continuar:

        break

    respostas += 1

    resposta_capital = input(f"Qual é a capital de {estado} ?")

    if resposta_capital.lower() == capital.lower():

        print("Resposta correta")

        acertos += 1

    else:

        print(f"Resposta incorreta, a capital de {estado} é {capital}")

    while True:

        resposta_continue = input(
            "Deseja continuar ? (s) para sim (n) para não"
        ).lower()

        if resposta_continue not in ["s", "n"]:

            print("Opção invalida, Digite (s) para continuar ou (n) para parar!")

            continue

        elif resposta_continue == "n":

            continuar = False

        break


porcentagem = acertos / respostas * 100


print(f"Voce acertou {acertos} de  {respostas} respostas")

print(f"voce acertou {porcentagem:.2f}%")
