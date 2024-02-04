"""Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:
Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 6.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina Diamante
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000 = Imortal
Se XP for maior ou igual a 10.001 = Radiante

Saída Ao final deve se exibir uma mensagem:
"O Herói de nome {nome} está no nível de {nivel}"
"""

nome = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de experiência (XP) do herói: "))

if xp < 1000:
    nivel = "Ferro"
elif 1001 <= xp <= 2000:
    nivel = "Bronze"
elif 2001 <= xp <= 5000:
    nivel = "Prata"
elif 5001 <= xp <= 6000:
    nivel = "Ouro"
elif 7001 <= xp <= 8000:
    nivel = "Platina Diamante"
elif 8001 <= xp <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

print(f"O Herói de nome {nome} está no nível de {nivel}")