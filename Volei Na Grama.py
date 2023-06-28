equipe1_nome1 = input()
equipe1_nome2 = input()
equipe2_nome1 = input()
equipe2_nome2 = input()
partidas = int(input())

print("VAMO VER QUEM VAI COMER GRAMA! TEREMOS " + partidas + " PARTIDAS ENTRE:")
print(equipe1_nome1 + " e " equipe1_nome2 + " X " + equipe2_nome1 + " e " + equipe2_nome2)

for i in range(0, partidas):
    pontos_equipe1 = input()
    pontos_equipe2 = input()