garrafas = 20
voluntarios = 5
inicio = "s"

while garrafas > 0 and inicio != "O InterCIn acabou!!! Vamos ver nosso estoque de bebidas":
    inicio = input()
    if inicio == "Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores":
        jogadores = int(input())
        if jogadores > garrafas:
            print("Não teremos água para todos os jogadores... Temos que garantir" + str((jogadores - garrafas)) + "garrafas")
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
        if garrafas < 0:
            print("Prometemos distribuir" + str(abs(garrafas)) + "garrafas e zeramos")


else:
    if garrafas > 0:
        print("Notícia boa: sobraram " + str(garrafas) + " garrafas, vamos guardar na geladeira :D")
    elif garrafas == 0:
        print("Vendemos todas as águas, fizemos uma contagem certeira!!")
    else:
        print("Estamos devendo " + str(abs(garrafas)) + " garrafas para os alunos...")


