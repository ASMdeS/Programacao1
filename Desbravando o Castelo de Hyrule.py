def resgate_zelda(elementos_salas, sala_inicial, contador_sala, link_espada, rupees_coletados):
    sala_analisada = elementos_salas[(sala_inicial + contador_sala) % quantidade_salas]
    if contador_sala == len(elementos_salas):
        return False, rupees_coletados
    else:
        for a in range(0, sala_analisada.count("◇")):
            rupees_coletados += 1
        if "Zelda" in sala_analisada:
            if "Agahnim" in sala_analisada:
                if link_espada:
                    return True, rupees_coletados
            else:
                return True, rupees_coletados
        else:
            if "espada" in sala_analisada:
                link_espada = True
            return resgate_zelda(elementos_salas, sala_inicial, contador_sala + 1, link_espada, rupees_coletados)

quantidade_salas = int(input())
elementos_salas = []
contador_sala = 0
link_espada = False
rupees_coletados = 0

for numero in range(quantidade_salas):
    sala_atual = input().split()
    elementos_salas.append(sala_atual)

sala_inicial = int(input())

print(resgate_zelda(elementos_salas, sala_inicial, contador_sala, link_espada, rupees_coletados))

resgatou_zelda, contagem_rupees = resgate_zelda(elementos_salas, sala_inicial, contador_sala, link_espada, rupees_coletados)

if resgatou_zelda:
    print(f'A princesa Zelda está a salvo e ainda conseguimos coletar {contagem_rupees} rupees')
else:
    print(f'Infelizmente a princesa ainda corre perigo, mas temos {contagem_rupees} rupees para nos ajudar nas buscas')