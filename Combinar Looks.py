#Opções de roupas
opcoes_penteados = input().split(" - ")
opcoes_tops = input().split(" - ")
opcoes_bottoms = input().split(" - ")
opcoes_sapatos = input().split(" - ")
print("Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!")

#Descobrir o meio

#Arrendondar para cima
meio_penteado = -(-len(opcoes_penteados) // 2)
meio_top = -(-len(opcoes_tops) // 2)
meio_bottom = -(-len(opcoes_bottoms) // 2)
meio_sapato = -(-len(opcoes_sapatos) // 2)

#Aumentar caso seja par
if len(opcoes_penteados) % 2 == 0:
    meio_penteado = meio_penteado + 1
if len(opcoes_tops) % 2 == 0:
    meio_top = meio_top + 1
if len(opcoes_bottoms) % 2 == 0:
    meio_bottom = meio_bottom + 1
if len(opcoes_sapatos) % 2 == 0:
    meio_sapato = meio_sapato + 1

#Ajustar para contagem começando em 0

meio_penteado = meio_penteado - 1
meio_top = meio_top - 1
meio_bottom = meio_bottom - 1
meio_sapato = meio_sapato - 1

saida = False

cursor_penteado = None
cursor_top = None
cursor_bottom = None
cursor_sapato = None
#Usando a máquina
while saida == False:
    selecao_penteado = None
    selecao_top = None
    selecao_bototm = None
    selecao_sapato = None
    selecao_barbie = input().split()
    if selecao_barbie[0][1] == "<":
        cursor_penteado = (int(meio_penteado) - int(selecao_barbie[0][0])) % len(opcoes_penteados)
        selecao_penteado = opcoes_penteados[cursor_penteado]
    elif selecao_barbie[0][1] == ">":
        cursor_penteado = (int(meio_penteado) + int(selecao_barbie[0][0])) % (len(opcoes_penteados))
        selecao_penteado = opcoes_penteados[cursor_penteado]

    if selecao_barbie[1][1] == "<":
        cursor_top = (int(meio_top) - int(selecao_barbie[1][0])) % len(opcoes_tops)
        selecao_top = opcoes_tops[cursor_top]
    elif selecao_barbie[1][1] == ">":
        cursor_top = (int(meio_top) + int(selecao_barbie[1][0])) % len(opcoes_tops)
        selecao_top = opcoes_tops[int(cursor_top)]

    if selecao_barbie[2][1] == "<":
        cursor_bottom = (int(meio_bottom) - int(selecao_barbie[2][0])) % len(opcoes_bottoms)
        selecao_bottom = opcoes_bottoms[cursor_bottom]
    elif selecao_barbie[2][1] == ">":
        cursor_bottom = (int(meio_bottom) + int(selecao_barbie[2][0])) % len(opcoes_bottoms)
        selecao_bottom = opcoes_bottoms[cursor_bottom]

    if selecao_barbie[3][1] == "<":
        cursor_sapato = (int(meio_sapato) - int(selecao_barbie[3][0])) % len(opcoes_sapatos)
        selecao_sapato = opcoes_sapatos[cursor_sapato]
    elif selecao_barbie[3][1] == ">":
        cursor_sapato = (int(meio_sapato) + int(selecao_barbie[3][0])) % len(opcoes_sapatos)
        selecao_sapato = opcoes_sapatos[cursor_sapato]
    print("Iniciando mesclagem...")
    print(f"""O look gerado foi:
cabelo {selecao_penteado}, {selecao_top} com {selecao_bottom} e {selecao_sapato} nos pés.""")
    opiniao_barbie = input()
    if opiniao_barbie == "Amei!!":
        if selecao_top == "camisa da seleção":
            print("Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!")
        else:
            print("Essa Barbie vai arrasar com o look perfeito!")
        saida = True
    elif opiniao_barbie == "Melhor escolher eu mesma":
        print("Acho que estou precisando de ajustes, Ken :(")
        saida = True
    meio_penteado = cursor_penteado
    meio_top = cursor_top
    meio_bottom = cursor_bottom
    meio_sapato = cursor_sapato