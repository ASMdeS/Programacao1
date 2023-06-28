jogos = int(input())
pontos_vencedor = 0
time_vencedor = "a"
total = 0
pontos = 0
numero = 0

while numero < jogos:
    pontos = 0
    time = input()
    gols = int(input())
    chutes = int(input())
    amarelos = int(input())
    vermelhos = int(input())
    pontos = pontos + (gols*10) + (chutes*0.3) - (amarelos*2) - (vermelhos*4)
    if vermelhos >= amarelos:
        pontos = pontos - 3
    if pontos < 0:
        print("O time " + time + " ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
        numero = jogos
    else:
        if pontos > pontos_vencedor:
            pontos_vencedor = pontos
            time_vencedor = time
        total = total + pontos
    if numero == (jogos - 1) and pontos_vencedor > 0:
        chance = ((pontos_vencedor/total)*100)
        percentage = ("%.2f" % chance)
        print("Com " + percentage + "% dos pontos, o time " + time_vencedor + " pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.")
    numero = numero + 1