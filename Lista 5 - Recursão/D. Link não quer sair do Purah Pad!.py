def queda_bloco(primeira_linha, segunda_linha):



matriz = []
numero_linhas = int(input())

for n in range(0, numero_linhas):
    entrada_linha = input()
    lista_linha = [letra for letra in entrada_linha]
    matriz.append(lista_linha)

entrada = None

while entrada != "sair":
    entrada = input()
    entrada.split(", ")
