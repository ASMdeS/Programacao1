#Função que retornará lista de todos os trigamas
def trigramas(frase_entrada, i, frase_tigrama):
    if i + 3 <= len(frase_entrada):
        frase_tigrama.append(frase_entrada[i:i+3])
        return trigramas(frase_entrada, i + 1, frase_tigrama)
    else:
        return frase_tigrama

#Função que irá comparar o primeiro termo
def comparar(entrada, buscada, index_entrada, index_buscada, frase_entrada, frase_buscada, boolean):
    print(entrada)
    print(buscada)
    if boolean is True:
        print("ddddddddddddddddddddddddddddddddddd")
        print(buscada[list(buscada.keys())[frase_buscada]][index_buscada])
        print(entrada[list(entrada.keys())[frase_entrada]][index_entrada])
        if buscada[list(buscada.keys())[frase_buscada]][index_buscada] == entrada[list(entrada.keys())[frase_entrada]][index_entrada]:
            print(boolean)
            return comparar(entrada, buscada, index_entrada + 1, index_buscada + 1, frase_entrada, frase_buscada, True)
    else:
        for trigrama in entrada[list(entrada.keys())[frase_entrada]]:
            print(trigrama)
            print(buscada[list(buscada.keys())[0]][0])
            if buscada[list(buscada.keys())[frase_buscada]][0] == trigrama:
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                return comparar(entrada, buscada, index_entrada, index_buscada + 1, frase_entrada, frase_buscada, True)
    return comparar(entrada, buscada, index_entrada, index_buscada, frase_entrada + 1, frase_buscada, False)

#Será usado
frase_entrada = None
dicionario_trigamas = dict()
dicionario_buscado = dict()

#Montar dicionário frases iniciais
while frase_entrada != "END_OF_FILE":
    frase_entrada = input()
    dicionario_trigamas[frase_entrada] = trigramas(frase_entrada.lower(), 0, [])

#quantidade de trechos
quantidade_trechos = int(input())

#Montar dicionário frases finais
for i in range(0, quantidade_trechos):
    frase_buscada = input()
    dicionario_buscado[frase_buscada] = trigramas(frase_buscada.lower(), 0, [])


print(comparar(dicionario_trigamas, dicionario_buscado, 0, 0, 0, 0, False))