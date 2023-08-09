nome_suspeito = input()
string_concat = input()
encontrou_suspeito = None
i = 0
j = 1
#Slice string

while i < len(string_concat) and encontrou_suspeito != nome_suspeito:
    while j < len(string_concat) + 1 and encontrou_suspeito != nome_suspeito:
        encontrou_suspeito = string_concat[i:(j)]
        print(encontrou_suspeito)
        j += 1
    #return substrings
    i += 1
    j = 1

#if
    #print(f'Encontrei, o culpado é o {nome_suspeito}!')
#else:
    #print()