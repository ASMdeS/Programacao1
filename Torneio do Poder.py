class Lutador:
    def __init__(self, nome, poder_luta, especie, incluido):
        self.nome = nome
        self.poder_luta = poder_luta
        self.especie = especie
        self.incluido = incluido

contagem_lutadores = 0
lista_lutadores = []

while contagem_lutadores < 8:
    entrada = input().split()
    if entrada[0] == "ADD":
        entrada[1] = Lutador(entrada[1], int(entrada[2]), entrada[3], True)
        contagem_lutadores +=1
        if entrada[3] == "Saiyajin":
            entrada[1].poder_luta += (entrada[1].poder_luta / 10)
            lista_lutadores.append(entrada[1])
        elif entrada[3] == "Hibrido-Saiyajin":
            entrada[1].poder_luta += (entrada[1].poder_luta / 5)
    elif entrada[0] == "DELL":
        entrada[1] = Lutador(entrada[1], int(entrada[2]), entrada[3], False)
        contagem_lutadores -= 1
        for elemento in lista_lutadores:
            if elemento == entrada[1]:
                lista_lutadores.pop(elemento.index())

primeira_chave = lista_lutadores[:3]
segunda_chave = lista_lutadores[4:]

