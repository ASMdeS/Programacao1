equipe1_nome1 = input()
equipe1_nome2 = input()
equipe2_nome1 = input()
equipe2_nome2 = input()
partidas = int(input())
pontos_equipe1 = 0
pontos_equipe2 = 0
pontostotais_equipe1 = 0
pontostotais_equipe2 = 0
vitorias_equipe1 = 0
vitorias_equipe2 = 0
numero = 0
total = 0
coeficiente_equipe1 = 0
coeficiente_equipe2 = 0
Encerrar = False

print("VAMO VER QUEM VAI COMER GRAMA! TEREMOS " + str(partidas) + " PARTIDAS ENTRE:")
print(equipe1_nome1 + " e " + equipe1_nome2 + " X " + equipe2_nome1 + " e " + equipe2_nome2)

while numero < partidas and Encerrar == False:
    pontos_equipe1 = int(input())
    pontos_equipe2 = int(input())
    pontostotais_equipe1 = pontostotais_equipe1 + pontos_equipe1
    pontostotais_equipe2 = pontostotais_equipe2 + pontos_equipe2
    if pontos_equipe1 == 0:
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA")
        Encerrar = True
    elif pontos_equipe2 == 0:
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA")
        Encerrar = True
    else:
        total = pontos_equipe1 + pontos_equipe2
        if pontos_equipe1 >= pontos_equipe2:
            vitorias_equipe1 = vitorias_equipe1 + 1
        else:
            vitorias_equipe2 = vitorias_equipe2 + 1
        numero = numero + 1
        if numero == partidas:
            total = pontostotais_equipe1 + pontostotais_equipe2
            coeficiente_equipe1 = pontostotais_equipe1*(vitorias_equipe1/partidas)
            coeficiente_equipe2 = pontostotais_equipe2 * (vitorias_equipe2/partidas)
            print("CARAMBA! Tivemos um total de " + str(total) + " bolas ao chão ao longo dessa disputa.")
            if coeficiente_equipe1 >= coeficiente_equipe2:
                print(equipe1_nome1 + " e " + equipe1_nome2 + " são os grandes vencedores!")
                print("Mataram " + str(pontostotais_equipe1) + " bolas, ganhando " + str(vitorias_equipe1) + " partidas")
            else:
                print(equipe2_nome1 + " e " + equipe2_nome2 + " são os grandes vencedores!")
                print("Mataram " + str(pontostotais_equipe2) + " bolas, ganhando " + str(vitorias_equipe2) + " partidas")