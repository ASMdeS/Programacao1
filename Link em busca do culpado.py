nome_suspeito = input()
string_concat = input()
encontrou_suspeito = ""
i = 0
j = 1
suspeito_encontrado = False
#Slice string

while i < len(string_concat) and encontrou_suspeito.lower() != nome_suspeito.lower():
    while j < len(string_concat) + 1 and encontrou_suspeito.lower() != nome_suspeito.lower():
        encontrou_suspeito = string_concat[i:(j)].lower()
        j += 1
    #return substrings
    i += 1
    j = 1
    if encontrou_suspeito.lower() == nome_suspeito.lower():
        suspeito_encontrado = True

if suspeito_encontrado == True:
    print(f'Encontrei, o culpado é o {nome_suspeito}!')
else:
    print(f'Não era o {nome_suspeito}, tenho que continuar procurando.')