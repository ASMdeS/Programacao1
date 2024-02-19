andares_comodos = int(input())
lista_final = []

for i in range(andares_comodos):
    lista_comodos = []
    for i in range(andares_comodos):
        tamanho_comodo = int(input())
        lista_comodos.append(tamanho_comodo)
    lista_final.append(lista_comodos)

for a in range(andares_comodos):
    print(*lista_final[a])