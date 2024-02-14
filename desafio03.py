# Meus amigos possuem os seguintes interesses:
#  • Gostam de programação: Ricardo, Roberto, Pedro, Vinicius
#  • Gostam de jogar futebol: Mateus, Roberto, Paulo, Vinicius
#  • Estudam na Asimov Academy: Ricardo, Mateus, Paulo, Pedro
#  Usando operações de conjunto, encontre o conjunto de amigos que gostam de programação e
#  estudam na Asimov Academy, mas que não gostam de jogar futebol.

conj_programacao = {'Ricardo', 'Roberto', 'Pedro', 'Vinicius'}
conj_futebol = {'Mateus', 'Roberto', 'Paulo', 'Vinicius'}
conj_asimov = {'Ricardo', 'Mateus', 'Paulo', 'Pedro'}

programacao_e_asimov = (conj_programacao | conj_asimov) - conj_futebol
print(programacao_e_asimov)