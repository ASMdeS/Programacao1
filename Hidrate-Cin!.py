garrafas = 20
voluntarios = 5
inicio = "a"

while garrafas >= 0 and inicio != "O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas":
    inicio = input()
    if inicio == "Acabou uma partida e precisamos da seguinte quantidade de garrafas para matar a sede dos jogadores":
        jogadores = int(input())
        if jogadores > garrafas:
            print("Não teremos água para todos os jogadores... Temos que garantir " + str((jogadores - garrafas)) + " garrafas!!")
            garrafas = garrafas*2
        garrafas = garrafas - jogadores
    elif inicio == "Encham o cooler! O jogo vai começar!!!!":
        garrafas = garrafas + 15
        print("Geladeira cheia!")
    elif inicio == "Timeout da partida! Verifiquem quantas garrafas pediram aos voluntários":
        quantidade_1 = int(input())
        quantidade_2 = int(input())
        quantidade_3 = int(input())
        quantidade_4 = int(input())
        quantidade_5 = int(input())
        quantidade_total = quantidade_1 + quantidade_2 + quantidade_3 + quantidade_4 + quantidade_5
        garrafas = garrafas - quantidade_total
        if quantidade_total > garrafas:
            print("Faltaram " + str(abs(garrafas)) + " garrafas para atender o pedido feito aos voluntários")
    if inicio == "O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas":
        if garrafas > 0:
            print("Sobraram " + str(garrafas) + " garrafas, vamos guardar na geladeira :D")
        elif garrafas == 0:
            print("Vendemos todas as garrafas! Nosso planejamento foi perfeito!")
    if garrafas < 0:
        print("Por questões logísticas, teremos que acabar com os jogos...")