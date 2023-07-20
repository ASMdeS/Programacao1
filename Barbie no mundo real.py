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

Zona_Norte = []
Zona_Sul = []
Zona_Leste = []
Zona_Oeste = []

numero_norte = 0
numero_sul = 0
numero_leste = 0
numero_oeste = 0

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

#Local capangas
posicao_capangas = input().split(" - ")
localizacao_capangas = posicao_capangas[0]
localizacao_quebrada = localizacao_capangas.split(" ")
distancia_capangas = posicao_capangas[1]
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


#Procura
for lugar in esconderijos_barbie:
    print(f"""Recebemos informações que a Barbie está no(a) {lugar} mais próximo(a)... Vá atrás dela!
Lista dos(as) {lugar}s mais proximos(as):""")
    indexes = [idx for idx, value in enumerate(lista_tipos) if value == lugar]
    print(indexes)
    for indice in indexes:
        contador_numerico = 1
        distancia_euclidiana = ((int((coordenadas_x[int(indice)])) - int(x_capangas))**2 + (int((coordenadas_y[int(indice)])) - int(y_capangas))**2)**0.5
        contador_numerico +=1
        lista_distancias.append(distancia_euclidiana)
        distancias_organizadas = sorted(lista_distancias)
        print(lista_distancias)
        print(distancias_organizadas)
    for item in distancias_organizadas:
        (f"{int(item)+1}. {lista_lugares[int(indice)]} ({lista_zonas[indice]}) - {distancia_euclidiana}")
