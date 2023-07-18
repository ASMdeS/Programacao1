#Opções de roupas
opcoes_penteados = input().split(" - ")
opcoes_tops = input().split(" - ")
opcoes_bottoms = input().split(" - ")
opcoes_sapatos = input().split(" - ")
print("Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!")




escolha_penteado =
escolha_top =
escolha_bottom =
escolha_sapato =
saida = False



#Usando a máquina
while saida == False:
    selecao_barbie = input().split()
    if selecao_barbie[0] == "1<":

    print("Iniciando mesclagem...")
    print(f"""O look gerado foi: 
    cabelo {escolha_penteado}, {escolha_top} com {escolha_bottom} e {escolha_sapato} nos pés.""")
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