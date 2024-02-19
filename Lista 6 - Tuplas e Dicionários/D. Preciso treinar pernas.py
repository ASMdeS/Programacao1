#Função que retornará lista de todos os trigamas
def trigramas(frase_entrada):
    frase_tigrama = []
    for i in range(len(frase_entrada) - 2):
        trigram = frase_entrada[i:i + 3]
        frase_tigrama.append(trigram)
    return frase_tigrama
#Será usado
frase_entrada = None
dicionario_trigamas = dict()
dicionario_buscado = dict()
achou = None

#Montar dicionário frases iniciais
while frase_entrada != "END_OF_FILE":
    frase_entrada = input()
    if frase_entrada != "END_OF_FILE":
        dicionario_trigamas[frase_entrada] = trigramas(frase_entrada.lower())

#quantidade de trechos
quantidade_trechos = int(input())

#Montar dicionário frases finais
for i in range(0, quantidade_trechos):
    frase_buscada = input()
    dicionario_buscado[frase_buscada] = trigramas(frase_buscada.lower())

#checar
for i in range(0, len(dicionario_buscado)):
    achou = False
    for j in range(0, len(dicionario_trigamas)):
        for trigrama in dicionario_trigamas[list(dicionario_trigamas.keys())[j]]:
            if trigrama == dicionario_buscado[list(dicionario_buscado.keys())[i]][0]:
                if len(dicionario_buscado[list(dicionario_buscado.keys())[i]]) < len(dicionario_trigamas[list(dicionario_trigamas.keys())[j]][dicionario_trigamas[list(dicionario_trigamas.keys())[j]].index(trigrama):]):
                    for k in range(0, len(dicionario_buscado[list(dicionario_buscado.keys())[i]])):
                        if dicionario_buscado[list(dicionario_buscado.keys())[i]][k] == dicionario_trigamas[list(dicionario_trigamas.keys())[j]][dicionario_trigamas[list(dicionario_trigamas.keys())[j]].index(trigrama)+k]:
                            if achou is not True and k == len(dicionario_buscado[list(dicionario_buscado.keys())[i]]) - 1:
                                print(j)
                                achou = True
    if achou is not True:
        print("-1")