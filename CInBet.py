jogos = int(input())
pontos_vencedor = 0
time_vencedor = "a"
total = 0
pontos = 1
numero = 0
ManCityPontos = 0
SpiceGirlsPontos = 0


while numero < jogos and pontos >=0:
    pontos = 0
    time = input()
    gols = int(input())
    chutes = int(input())
    amarelos = int(input())
    vermelhos = int(input())
    for a in range(0, gols):
        pontos = pontos + 10
    for b in range(0, chutes):
        pontos = pontos + 3
    for c in range(0, amarelos):
        pontos = pontos - 2
    for d in range(0, vermelhos):
        pontos = pontos - 4
    if gols >= (chutes*0.3):
        pontos = pontos + 3
    if vermelhos >= amarelos:
        pontos = pontos - 3
    if time == "Manchester CIn":
        ManCityPontos = ManCityPontos + pontos
        total = total + pontos
    elif time == "SpiCIn Girls":
        SpiceGirlsPontos = SpiceGirlsPontos + pontos
        total = total + pontos
    if pontos < 0:
        print("O time " + time + " ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
    if numero == (jogos - 1) and pontos > 0:
        if ManCityPontos > SpiceGirlsPontos:
            time_vencedor = "Manchester CIn"
            pontos_vencedor = ManCityPontos
            chance = ((pontos_vencedor / total) * 100)
            percentage = ("%.2f" % chance)
            print(
                "Com " + percentage + "% dos pontos, o time " + time_vencedor + " pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.")
        elif SpiceGirlsPontos > ManCityPontos:
            time_vencedor = "SpiCIn Girls"
            pontos_vencedor = SpiceGirlsPontos
            chance = ((pontos_vencedor / total) * 100)
            percentage = ("%.2f" % chance)
            print(
                "Com " + percentage + "% dos pontos, o time " + time_vencedor + " pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.")

    numero = numero + 1