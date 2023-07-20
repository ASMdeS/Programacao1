local_capangas = None
lista_locais = []
entrada = None



while entrada != "FIM":
    entrada = input()
    if entrada != "FIM":
        local_capangas = entrada.split(" - ")
        lista_locais.append(local_capangas)
    else:
        saida = True
    for n in lista_locais:
        print(f"""
Zona Norte:""")
        numero_norte = 0
        numero_sul = 0
        numero_leste = 0
        numero_oeste = 0
        if lista_locais[int(n)][0] == "Norte":
            print({lista_locais[int(n)][1]}
            numero_norte += 1
        if numero_norte == 0:
            print("Nenhum local mapeado nessa zona!")

        print(f"""
Zona Sul:""")
        if lista_locais[int(n)][0] == "Sul":
            print({lista_locais[int(n)][1]}
            numero_sul += 1
        if numero_sul == 0:
            print("Nenhum local mapeado nessa zona!")

        print(f"""
Zona Leste:""")
        if lista_locais[int(n)][0] == "Leste":
            print({lista_locais[int(n)][1]}
        numero_leste += 1
        if numero_leste == 0:
            print("Nenhum local mapeado nessa zona!")

        print(f"""
Zona Oeste:""")
        if lista_locais[int(n)][0] == "Oeste":
            print({lista_locais[int(n)][1]}
        numero_oeste += 1
        if numero_oeste == 0:
            print("Nenhum local mapeado nessa zona!")

esconderijos_barbie = input().split()
posicao_capangas = input().split(" - ")
localizacao_capangas = posicao_capangas[0]
distancia_capangas = posicao_capangas[1]

distancia_euclidiana = ((x1 – x2)**2) + ((y1 – y2)**2)**0.5


print(lista_locais)