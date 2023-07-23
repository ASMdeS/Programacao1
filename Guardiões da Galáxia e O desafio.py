numero_frases = int(input())

#Checar se a entrada é um palíndromo
def checar_palindromo(entrada_original):
    return entrada_original.lower().replace(" ", "") == entrada_original.lower().replace(" ", "")[::-1]

#Contar caracteres distintos:
def contar_distintos(entrada_original):
    string_vazia = ""
    for caractere in entrada_original.lower().replace(" ", ""):
        if caractere not in string_vazia:
            string_vazia += caractere
    if entrada_original.isdigit():
        print(f'Há {len(string_vazia)} número(s) distinto(s) na sequência de números.')
    else:
        print(f'Há {len(string_vazia)} letra(s) distinta(s) na frase.')
#Loop
for n in range(0, numero_frases):
    entrada_original = input()
    if checar_palindromo(entrada_original):
        if entrada_original.isdigit():
            print(f'O número "{entrada_original}" é um palíndromo!')
            contar_distintos(entrada_original)
        else:
            print(f'A frase "{entrada_original}" é um palíndromo!')
            contar_distintos(entrada_original)
    else:
        print(f'A frase ou o número não é um palíndromo.')