#Inputs
posicao_capsulas = eval(input())
posicao_explosao = eval(input())
raio_impacto = int(input())

#Listas que serão usadas
posicao_central = []
lista_sobreviventes = []

#Ponto Central
def ponto_central(lista_x, lista_y):
    return [(sum(lista_x) / len(lista_x)), (sum(lista_y) / len(lista_y))]

#Checar sobrevivência
def checar_sobrevivencia(capsula, astronauta):
    return raio_impacto < ((posicao_capsulas[capsula][astronauta][0] - posicao_explosao[0]) ** 2 + (posicao_capsulas[capsula][astronauta][1] - posicao_explosao[1]) ** 2) ** (1 / 2)

#Resgatar os astronautas
def resgatar_astronautas():
    for capsula in range(0, len(posicao_capsulas)):
        lista_x = []
        lista_y = []
        for astronauta in range(0, len(posicao_capsulas[capsula])):
            if checar_sobrevivencia(capsula, astronauta):
                lista_x.append(posicao_capsulas[capsula][astronauta][0])
                lista_y.append(posicao_capsulas[capsula][astronauta][1])
                lista_sobreviventes.append(posicao_capsulas[capsula][astronauta])
        if len(lista_x) > 0:
            posicao_central.append(ponto_central(lista_x, lista_y))
    return [len(lista_sobreviventes), posicao_central]

#Printar
print(resgatar_astronautas())