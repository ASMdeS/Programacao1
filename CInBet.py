jogos = int(input())
pontos = 0

for i in range(0, jogos):
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






