class Lutador:
    def __init__(self, nome, poder_luta, especie, incluido):
        self.nome = nome
        self.poder_luta = poder_luta
        self.especie = especie
        self.incluido = incluido

    def aumentar_poder(self):
        if self.especie == "Saiyajin":
            self.poder_luta += (self.poder_luta / 10)
        elif self.especie == "Hibrido-Saiyajin":
            self.poder_luta += (self.poder_luta / 5)


contagem_lutadores = 0
lista_objetos = []

while contagem_lutadores < 8:
    entrada = input().split()
    if entrada[0] == "ADD":
        entrada[1] = Lutador(entrada[1], int(entrada[2]), entrada[3], True)
        lista_objetos.append(entrada[1])
        contagem_lutadores += 1
    elif entrada[0] == "DEL":
        for elemento in lista_objetos:
            if elemento.nome == entrada[1]:
                lista_objetos.remove(elemento)
        contagem_lutadores -= 1

primeira_chave = lista_objetos[0:4]
segunda_chave = lista_objetos[4:8]

# Quartas
for i in range(0, 4):
    if primeira_chave[i].poder_luta > segunda_chave[i].poder_luta:
        primeira_chave[i].aumentar_poder()
        segunda_chave.pop(i)
    else:
        segunda_chave[i].aumentar_poder()
        primeira_chave.pop(i)

for objeto in primeira_chave:
    print(objeto.nome)
for objeto in segunda_chave:
    print(objeto.nome)