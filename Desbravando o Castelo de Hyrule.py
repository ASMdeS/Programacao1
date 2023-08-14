quantidade_salas = int(input())
elementos_salas = []
resgatou_zelda = False
link_espada = False
rupees_coletados = 0

for numero in range(quantidade_salas):
    sala_atual = input().split()
    elementos_salas.append(sala_atual)

sala_inicial = int(input())

for sala in range(quantidade_salas):
    sala_analisada = elementos_salas[(sala_inicial+sala) % quantidade_salas]
    if "Zelda" in sala_analisada:
        if "Agahnim" in sala_analisada:
            if link_espada:
                resgatou_zelda = True
        else:
            resgatou_zelda = True
    if "espada" in sala_analisada:
        link_espada = True
    for a in range(0, sala_analisada.count("◇")):
        rupees_coletados += 1

if resgatou_zelda:
    print(f'A princesa Zelda está a salvo e ainda conseguimos coletar {rupees_coletados} rupees')
else:
    print(f'Infelizmente a princesa ainda corre perigo, mas temos {rupees_coletados} rupees para nos ajudar nas buscas')