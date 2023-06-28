jogos = int(input())
pontos_vencedor = 0
time_vencedor = "a"
total = 0


for i in range(0, jogos):
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
    if pontos < 0:
        print("O time " + time + " ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
    else:
        if pontos > pontos_vencedor:
            pontos_vencedor = pontos
            time_vencedor = time
        total = total + pontos
if pontos_vencedor > 0:
    chance = ((pontos_vencedor/total)*100)
    percentage = ("%.2f" % chance)
    print("Com " + percentage + "% dos pontos, o time Manchester CIn pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.")