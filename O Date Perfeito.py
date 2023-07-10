lista_desejados = input().split(", ")
lista_casa = input().split(", ")
interseccao_listas = [elemento for elemento in lista_desejados if elemento in lista_casa]
quantidade_comprar = len(lista_desejados) - len(interseccao_listas)
quantidade_desejados = len(lista_desejados)

if quantidade_comprar == quantidade_desejados:
    print(f"Nossa, irei ao shopping agora mesmo! Não tenho nenhum dos {quantidade_desejados} itens em casa.")
else:
    print("Esses são os itens que já tenho em casa:")
    for i in range(len(interseccao_listas)):
        print(str(i + 1) + "º item: " + interseccao_listas[i])
    if quantidade_comprar > 0:
        print(f"Irei precisar comprar {str(quantidade_comprar)} itens antes do meu encontro!")
    else:
        print(f"Que ótimo, consegui encontrar cada um dos {str(quantidade_desejados)} itens!")

print("Isso é tudo! Hora de me preparar!")