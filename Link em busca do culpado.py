#Função
def procurar(i, j, nome_suspeito, string_concat):
    encontrou_suspeito = string_concat[i:j]
    if j == len(string_concat):
        return procurar(i + 1, 1, nome_suspeito, string_concat)
    if i > len(string_concat):
        return False
    if encontrou_suspeito == nome_suspeito:
        return True
    else:
        return procurar(i, j + 1, nome_suspeito, string_concat)

#Argumentos
suspeito_original = input()
nome_suspeito = suspeito_original.lower()
string_concat = input().lower()
i = 0
j = 1

#Printar
if procurar(i, j, nome_suspeito, string_concat):
    print(f'Encontrei, o culpado é o {suspeito_original}!')
else:
    print(f'Não era o {suspeito_original}, tenho que continuar procurando.')