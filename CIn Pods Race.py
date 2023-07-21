
def caracteristicas(input().split(" ")):
    primeira_entrada = input().split(" ")
    nome_participante = primeira_entrada[0]
    qtd_propulsores = int(primeira_entrada[1])
    velocidade_propulsor = int(primeira_entrada[2])

novo_participante()

velocidade_inicial = qtd_propulsores * velocidade_propulsor
saida = False


while saida is False:
    entradas_subsequentes = input()
    if entradas_subsequentes == "Pit-Stop Espacial":
        qtd_propulsores += 1
    elif entradas_subsequentes == "Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.":
        qtd_propulsores -= 1
    elif entradas_subsequentes == "Opa esse participante não está inscrito, desclassificando em 3, 2, 1...":
        print(f"O {nome_participante} achou que não descobriríamos, tirem {nome_participante} imediatamente da pista.")
        saida = True
    elif entradas_subsequentes == "Próximo":
        velocidade_final = qtd_propulsores * velocidade_propulsor
        print(f""""--- Partipante: {nome_participante} ---
Qtd de propulsores Final: {qtd_propulsores}
Velocidade Inicial: {velocidade_inicial} km/h
Velocidade Final: {velocidade_final} km/h""")
        novo_participante()
