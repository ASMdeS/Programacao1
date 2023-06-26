inicio = input()
garrafas = 20
voluntarios = 5

while garrafas >0:
    if inicio == "Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores":
        jogadores = int(input())
        if jogadores > garrafas:
            print("Não teremos água para todos os jogadores... Temos que garantir" + (jogadores - garrafas) + "garrafas")
    elif inicio == "Encham o cooler, vai começar um jogo!!!!":
        garrafas = garrafas + 15
        print("Geladeira cheia!")
    elif inicio == "Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário":
        quantidade_1 = int(input())
        quantidade_2 = int(input())
        quantidade_3 = int(input())
        quantidade_4 = int(input())
        quantidade_5 = int(input())
        garrafas = garrafas - (quantidade_1 + quantidade_2 + quantidade_3 + quantidade_4 + quantidade_5)
        if garrafas <0:
            print("Prometemos distribuir" + abs(garrafas) + "garrafas e zeramos")

else:


