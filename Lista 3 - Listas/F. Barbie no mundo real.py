local_capangas = None
lista_locais = []
lista_zonas = []
lista_lugares = []
lista_tipos = []
lista_coordenadas = []
entrada = None
coordenadas_quebradas = []
coordenadas_x = []
coordenadas_y = []
percurso_barbie = 0

Zona_Norte = []
Zona_Sul = []
Zona_Leste = []
Zona_Oeste = []


print("Cidade mapeada:")

while entrada != "Fim":
    entrada = input()
    if entrada == "Fim":
        #Printar Zona Norte
        print(f"""
Zona Norte""")
        if len(Zona_Norte) > 0:
            for a in range(0, len(Zona_Norte)):
                print(f"- {Zona_Norte[int(a)][0]}")
        else:
            print("Nenhum local mapeado nessa zona!")
        #Printar Zona Sul
        print(f"""
Zona Sul""")
        if len(Zona_Sul) > 0:
            for a in range(0, len(Zona_Sul)):
                print(f"- {Zona_Sul[int(a)][0]}")
        else:
            print("Nenhum local mapeado nessa zona!")
        # Printar Zona Leste
        print(f"""
Zona Leste""")
        if len(Zona_Leste) > 0:
            for a in range(0, len(Zona_Leste)):
                print(f"- {Zona_Leste[int(a)][0]}")
        else:
            print("Nenhum local mapeado nessa zona!")
        # Printar Zona Oeste
        print(f"""
Zona Oeste""")
        if len(Zona_Oeste) > 0:
            for a in range(0, len(Zona_Oeste)):
                print(f"- {Zona_Oeste[int(a)][0]}")
        else:
            print("Nenhum local mapeado nessa zona!")
    else:
        local_capangas = entrada.split(" - ")
        lista_locais.append(local_capangas)
        lista_zonas.append(local_capangas[0])
        lista_lugares.append(local_capangas[1])
        lista_coordenadas.append(local_capangas[2])
        #Lista Zona Norte
        if local_capangas[0] == "Norte":
                Zona_Norte.append(local_capangas[1:])
        #Lista Zona Sul
        if local_capangas[0] == "Sul":
                Zona_Sul.append(local_capangas[1:])
        #Lista Zona Leste
        if local_capangas[0] == "Leste":
                Zona_Leste.append(local_capangas[1:])
        #Lista Zona Oeste
        if local_capangas[0] == "Oeste":
                Zona_Oeste.append(local_capangas[1:])

#Esoncerijos da Barbie
esconderijos_barbie = input().split(", ")
percurso_barbie = 0

#Local capangas
posicao_capangas = input().split(" - ")
localizacao_capangas = posicao_capangas[0]
localizacao_quebrada = localizacao_capangas.split(" ")
distancia_capangas = int(posicao_capangas[1])
x_capangas = localizacao_quebrada[0]
y_capangas = localizacao_quebrada[1]

#Pegando as coordenadas
for i in range(0, len(lista_lugares)):
    lugar_trabalho = (lista_lugares[int(i)].split(" "))
    lista_tipos.append(lugar_trabalho[0])

#Pegando os tipos de lugares
for a in range(0, len(lista_coordenadas)):
    coordenada_trabalho = (lista_coordenadas[int(a)].split(" "))
    coordenadas_x.append(coordenada_trabalho[0])
    coordenadas_y.append(coordenada_trabalho[1])

#Trabalhando com coordenadas
for coordenada in range(0, len(coordenadas_quebradas)):
    if((coordenadas_quebradas[int(coordenada)]) % 2) == 0:
        coordenadas_x.append(coordenadas_quebradas[int(coordenada)])
    else:
        coordenadas_y.append(coordenadas_quebradas[int(coordenada)])

#Lista_distancias
lista_distancias = []
distancias_organizadas = []
lista_tudo = []
lista_listas = []
tudo_organizado = []
saida = False

while saida is False:
    #Procura
    indexes = [idx for idx, value in enumerate(lista_tipos) if value == esconderijos_barbie[0]]
    if len(indexes) == 0:
        print(f"Nenhum(a) {esconderijos_barbie[0]} encontrado na cidade! que tipo de informação é essa!?")
    else:
        print(f"""
Recebemos informações que a Barbie está no(a) {esconderijos_barbie[0]} mais próximo(a)... Vá atrás dela!""")
        print(f"Lista dos(as) {esconderijos_barbie[0]}s mais proximos(as):")
        for indice in indexes:
            lista_tudo = []
            distancia_euclidiana = ((int((coordenadas_x[int(indice)])) - int(x_capangas))**2 + (int((coordenadas_y[int(indice)])) - int(y_capangas))**2)**0.5
            lista_distancias.append(distancia_euclidiana)
            lista_tudo.append(distancia_euclidiana)
            lista_tudo.append(f"{lista_lugares[int(indice)]} ({lista_zonas[int(indice)]})")
            lista_tudo.append((coordenadas_x[int(indice)]))
            lista_tudo.append((coordenadas_y[int(indice)]))
            lista_listas.append(lista_tudo)
            distancias_organizadas = sorted(lista_distancias)
        tudo_organizado = sorted(lista_listas)
        for item in range(0, len(tudo_organizado)):
            print(f"{int(item)+1}. {(tudo_organizado[item][1])} - {(tudo_organizado[item][0]):.2f}km")
        percurso_barbie = float(distancias_organizadas[0])
        if percurso_barbie > int(distancia_capangas):
            print("Não temos combustível suficiente para continuar a perseguição, infelizmente a Barbie conseguiu fugir!")
            saida = True
        else:
            print(f"Os capangas chegaram a(ao) {(tudo_organizado[0][1])}, mas a Barbie não estava mais lá...")
        x_capangas = int(tudo_organizado[0][2])
        y_capangas = int(tudo_organizado[0][3])



    contador_numerico = 2

    while saida is False:
        for lugar in esconderijos_barbie[1:]:
            contador_numerico += 1
            lista_listas = []
            tudo_organizado = []
            lista_distancias = []
            distancias_organizadas = []
            distancia_euclidiana = []
            indices = [idxes for idxes, value in enumerate(lista_tipos) if value == lugar]
            if len(indices) == 0:
                if contador_numerico == len(esconderijos_barbie):
                    print(f"Não tem nenhum(a) {lugar} no mapa e acabamos a lista de lugares, não sabemos pra onde ir... A Barbie fugiu!")
                    saida = True
                else:
                    print(f"Nenhum(a) {lugar} encontrado na cidade! que tipo de informação é essa!?")
            else:
                print(f"""
Recebemos informações que a Barbie fugiu para o(a) {lugar} mais distante... Vá atrás dela!""")
                print(f"Lista dos(as) {lugar}s mais distantes:")
                for index in indices:
                    lista_tudo = []
                    distancia_euclidiana = ((int((coordenadas_x[int(index)])) - int(x_capangas)) ** 2 + (int((coordenadas_y[int(index)])) - int(y_capangas)) ** 2) ** 0.5
                    lista_distancias.append(distancia_euclidiana)
                    lista_tudo.append(distancia_euclidiana)
                    lista_tudo.append(f"{lista_lugares[int(index)]} ({lista_zonas[int(index)]})")
                    lista_tudo.append((coordenadas_x[int(index)]))
                    lista_tudo.append((coordenadas_y[int(index)]))
                    lista_listas.append(lista_tudo)
                    distancias_organizadas = sorted(lista_distancias)
                tudo_organizado = sorted(lista_listas)
                x_capangas = int(tudo_organizado[len(tudo_organizado)-1][2])
                y_capangas = int(tudo_organizado[len(tudo_organizado)-1][3])
                for i in reversed(range(0, len(tudo_organizado))):
                    print(f"{(-(int(i)-len(tudo_organizado)))}. {(tudo_organizado[i][1])} - {(tudo_organizado[i][0]):.2f}km")
                percurso_barbie += float(distancias_organizadas[len(distancias_organizadas)-1])
                if percurso_barbie > int(distancia_capangas):
                    print("Não temos combustível suficiente para continuar a perseguição, infelizmente a Barbie conseguiu fugir!")
                    saida = True
                else:
                    if contador_numerico != len(esconderijos_barbie):
                        print(f"Os capangas chegaram a(ao) {(tudo_organizado[len(tudo_organizado)-1][1])}, mas a Barbie não estava mais lá...")
                    else:
                        print(f"Finalmente, depois de {percurso_barbie:.2f}km percorridos, os capangas capturaram a Barbie no(a) {(tudo_organizado[len(tudo_organizado)-1][1])} - Coordenadas:({(tudo_organizado[len(tudo_organizado)-1][2])}, {(tudo_organizado[len(tudo_organizado)-1][3])})")
                        saida = True
    saida = True