aluno = input()
professor = input()
vitorias_aluno = 0
vitorias_professor = 0

print("E agora, só pela resenha")
print("Melhor de 3 entre: " + aluno + " e " + professor + "!")
print("COMEÇOU!")

while vitorias_aluno < 1 and vitorias_professor < 1:
    pontos_aluno = 0
    pontos_professor = 0
    while pontos_aluno < 11 and pontos_professor < 11 or pontos_professor + 2 > pontos_aluno or pontos_aluno + 2 > pontos_professor:
        num = int(input())
        if (num % 2) == 0:
            pontos_professor = pontos_professor + 1
        else:
            pontos_aluno = pontos_aluno + 1
        if pontos_aluno == 11:
            if pontos_professor + 2 <= pontos_aluno:
                vitorias_aluno = vitorias_aluno + 1
                print(str(pontos_aluno) + " - " + str(pontos_professor))
                print(aluno + " ganhou esta partida!")
                print("Placar:" + aluno + vitorias_aluno + " - " + professor + vitorias_professor)
        elif pontos_professor == 11:
            if pontos_aluno + 2 <= pontos_professor:
                vitorias_professor = vitorias_professor + 1
                print(str(pontos_aluno) + " - " + str(pontos_professor))
                print(professor + " ganhou esta partida!")
                print("Placar:" + aluno + str(vitorias_aluno) + " - " + professor + str(vitorias_professor))
    if vitorias_professor == 2:
        print("FIM DA SÉRIE!")
        print(professor + " ganhou a série! A experiência ganhou!")
    elif vitorias_aluno == 2:
        print("FIM DA SÉRIE!")
        print(aluno + " ganhou a série! Puro talento!")