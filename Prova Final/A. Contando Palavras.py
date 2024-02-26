# Recebendo a entrada
entrada = input()

# Transformando a entrada em uma lista
lista_palavras = entrada.split()

# Criando um dicionário
dicionario_palavras = {}

# Definindo as palavras como chave e a ocorrência como valores
for palavra in lista_palavras:
    if palavra in dicionario_palavras:
        dicionario_palavras[palavra] += 1
    else:
        dicionario_palavras[palavra] = 1

# Imprimindo o dicionário no formato desejado
for chave, valor in dicionario_palavras.items():
    print(f'{chave}: {valor}')