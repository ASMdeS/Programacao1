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
    meio_top = meio_penteado + 1
if len(opcoes_bottoms) % 2 == 0:
    meio_bottom = meio_penteado + 1
if len(opcoes_sapatos) % 2 == 0:
    meio_sapato = meio_penteado + 1

#Ajustar para contagem começando em 0

meio_penteado = meio_penteado - 1
meio_top = meio_top - 1
meio_bottom = meio_bottom - 1
meio_sapato = meio_sapato - 1

selecao_penteado = None
selecao_top = None
selecao_bottom = None
selecao_sapato = None
selecao_total = []

print(meio_penteado)
print(meio_top)
print(meio_bottom)
print(meio_sapato)

saida = False

#Usando a máquina
while saida == False:
    selecao_barbie = input().split()
    print(selecao_barbie)
    if selecao_barbie[0][1] == "<":
        cursor = int(meio_penteado) - int(selecao_barbie[0][0])
        selecao_penteado = opcoes_penteados[cursor]
    elif selecao_barbie[0][1] == ">":
        cursor = int(meio_penteado) + int(selecao_barbie[0][0])
        selecao_penteado = opcoes_penteados[cursor]

    if selecao_barbie[1][1] == "<":
        cursor = int(meio_top) - int(selecao_barbie[1][0])
        selecao_top = opcoes_tops[cursor]
    elif selecao_barbie[1][1] == ">":
        cursor = int(meio_top) + int(selecao_barbie[1][0])
        selecao_top = opcoes_tops[cursor]

    if selecao_barbie[2][1] == "<":
        cursor = int(meio_bottom) - int(selecao_barbie[2][0])
        selecao_bottom = opcoes_bottoms[cursor]
    elif selecao_barbie[2][1] == ">":
        cursor = int(meio_bottom) + int(selecao_barbie[2][0])
        selecao_bottom = opcoes_bottoms[cursor]

    if selecao_barbie[3][1] == "<":
        cursor = int(meio_sapato) - int(selecao_barbie[3][0])
        selecao_sapato = opcoes_sapatos[cursor]
    elif selecao_barbie[3][1] == ">":
        cursor = int(meio_sapato) + int(selecao_barbie[3][0])
        selecao_sapato = opcoes_sapatos[cursor]
    print("Iniciando mesclagem...")
    print(f"""O look gerado foi: 
    cabelo {selecao_penteado}, {selecao_top} com {selecao_bottom} e {selecao_sapato} nos pés.""")
    opiniao_barbie = input()
    if opiniao_barbie == "Amei!!":
        if escolha_top == "camisa da seleção":
            print("Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!")
        else:
            print("Essa Barbie vai arrasar com o look perfeito!")
        saida = True
    elif opiniao_barbie == "Melhor escolher eu mesma":
        print("Acho que estou precisando de ajustes, Ken :(")
        saida = True