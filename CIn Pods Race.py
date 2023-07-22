novo_item = True
saida = False
participante_classificado = []
participante_desclassificado = []

def imprimir_relatorio():
    velocidade_final = qtd_propulsores * velocidade_propulsor
    print(f"""--- Participante: {nome_participante} ---
Qtd de propulsores Final: {qtd_propulsores}
Velocidade Inicial: {velocidade_inicial} km/h
Velocidade Final: {velocidade_final} km/h""")
    participante_classificado.append(nome_participante)

while novo_item is True:
    saida = False
    primeira_entrada = input().split(" ")
    nome_participante = primeira_entrada[0]
    qtd_propulsores = int(primeira_entrada[1])
    velocidade_propulsor = int(primeira_entrada[2])
    velocidade_inicial = qtd_propulsores * velocidade_propulsor
    while saida is False:
        entradas_subsequentes = input()
        if entradas_subsequentes == "Pit-Stop Espacial":
            qtd_propulsores += 1
        elif entradas_subsequentes == "Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.":
            qtd_propulsores -= 1
        elif entradas_subsequentes == "Opa esse participante não está inscrito, desclassificando em 3, 2, 1...":
            print(f"O {nome_participante} achou que não descobriríamos, tirem {nome_participante} imediatamente da pista.")
            saida = True
            participante_desclassificado.append(nome_participante)
        elif entradas_subsequentes == "Próximo":
            imprimir_relatorio()
            saida = True
        elif entradas_subsequentes == "FIM":
            imprimir_relatorio()
            saida = True
            novo_item = False
        if qtd_propulsores == 0:
            print(f"BUUMM!! Infelizmente, {nome_participante} está fora da corrida.")
            saida = True
            participante_desclassificado.append(nome_participante)
    if novo_item is False:
        if len(participante_classificado) > 0:
            print(f"Relatório da CIn Pod Race: {len(participante_classificado)} participantes terminaram a corrida e {len(participante_desclassificado)} foram desclassificados.")
        else:
            print("NÃO! Esses Droides me pagam, sabotaram minha corrida!")