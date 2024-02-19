time_casa = input()
time_fora = input()
vitorias_casa = 0
vitorias_fora = 0
rodada = 0

while vitorias_casa <3 and vitorias_fora <3:
    pontuação_do_time_casa = int(input())
    pontuação_do_time_fora = int(input())
    rodada = rodada + 1
    if pontuação_do_time_casa > pontuação_do_time_fora:
        vitorias_casa = vitorias_casa + 1
        print("O vencedor da " + str(rodada) + "ª rodada foi: " + time_casa)
    else:
        vitorias_fora = vitorias_fora + 1
        print("O vencedor da " + str(rodada) + "ª rodada foi: " + time_fora)
else:
    if vitorias_casa > vitorias_fora:
        print("O time " + time_casa + " ganhou a partida final!")
    else:
        print("O time " + time_fora + " ganhou a partida final!")