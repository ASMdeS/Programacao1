#Função que retornará lista de todos os trigamas
def trigramas(frase_entrada, i, frase_tigrama):
    if i + 3 <= len(frase_entrada):
        frase_tigrama.append(frase_entrada[i:i+3])
        return trigramas(frase_entrada, i + 1, frase_tigrama)
    else:
        return frase_tigrama

#Função que irá comparar o primeiro termo
def comparar(entrada, buscada, i):
    print(entrada)
    print(buscada)
    for trigrama in entrada[list(entrada.keys())[i]]:
        if buscada[list(buscada.keys())[0]] == trigrama:
            if buscada == entrada[entrada.index(trigrama):len(buscada)+1]:
                return i
    else:
        return comparar(entrada, buscada, i + 1, j, contador_correto)

def certeza(j, ):
    if buscada[list(buscada.keys())[j]] == entrada[list(entrada.keys())[i]]:
        return f
    else:

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


comparar(dicionario_trigamas, dicionario_buscado, 0)
