# Remover as letras de uma string
def remover_letras(string_remocao):
    resposta = ''
    for caractere in string_remocao:
        if caractere.isdigit():
            resposta += caractere
    return int(resposta)


# Passar a contagem do tempo para minutos
def contagem_tempo(string_contagem):
    duracao_treino = string_contagem.split()
    numero_tempo = duracao_treino[0]
    tipo_contagem = duracao_treino[1]
    if tipo_contagem == "segundos" or tipo_contagem == "segundo":
        return int(numero_tempo) / 60
    elif tipo_contagem == "horas" or tipo_contagem == "hora":
        return int(numero_tempo) * 60
    else:
        return int(numero_tempo)


# Julgar o suspeito para descobrir se é Natural ou não
def julgamento(suspeito):
    pontos = 0
    if suspeito["Biceps"] > 45:
        pontos += 1
    if suspeito["Treino"] < 30:
        pontos += 1
    if suspeito["Frequencia"] < 4:
        pontos += 1
    if suspeito["BF"] < 10:
        pontos += 1
    if suspeito["Suor"] == "Seco":
        pontos += 1
    if pontos > 2:
        return True
    else:
        return False


# Descobrindo a quantidade de fake_natties e sua proporção em relação ao total
def nattymeter(dicionario):
    fake_natties = 0
    for valor in dicionario.values():
        if julgamento(valor):
            fake_natties += 1
    if fake_natties == 0:
        print("Oh yeah, vivemos em uma sociedade sem suco, um great day")
    else:
        print(f'NOOO! {int((fake_natties / len(dicionario)) * 100)}% USARAM O SUCO')


# Criando o dicionário onde serão armazenados os famosos
dicionario_famosos = {}

# Criando o que servirá para entrada
entrada = None

# Pegando as entradas e preenchendo o dicionário utilizando as funções
while entrada != "FIM":
    entrada = input()
    if entrada == "Adicionar suspeito":
        nome_suspeito = input()
        dicionario_famosos[nome_suspeito] = {"Nome": nome_suspeito, "Biceps": 0, "Treino": 30,
                                             "Frequencia": 4, "BF": 10, "Suor": "Seco"}
        print(f'Novo suspeito: {nome_suspeito}')
    elif entrada == "Atualizar suspeito":
        caracteristicas_suspeito = input().split("-> ")
        nome_analisado = caracteristicas_suspeito[0]
        if nome_analisado in dicionario_famosos:
            lista_caracteristicas = caracteristicas_suspeito[1].split(", ")
            for caracteristica in lista_caracteristicas:
                chave_valor = caracteristica.split(': ')
                if chave_valor[0] == "Suor":
                    dicionario_famosos[nome_analisado][chave_valor[0]] = chave_valor[1]
                elif chave_valor[0] == "Treino":
                    dicionario_famosos[nome_analisado][chave_valor[0]] = contagem_tempo(chave_valor[1])
                else:
                    dicionario_famosos[nome_analisado][chave_valor[0]] = remover_letras(chave_valor[1])
        else:
            print("Quem é esse crazy man? Não tá aqui na database")
    elif entrada == "Julgamento":
        suspeito_analisar = input()
        if suspeito_analisar in dicionario_famosos.keys():
            print(f'Eu já tenho o meu veredito, e o meu veredito, {suspeito_analisar}:')
            if julgamento(dicionario_famosos[suspeito_analisar]):
                print("FAKE NATTY! USOU O SUCO!")
            else:
                print("Natural")
        else:
            print("Quem é esse crazy man? Não tá aqui na database")
    elif entrada == "NattyMeter":
        print("NattyMeter, ON!")
        nattymeter(dicionario_famosos)
    elif entrada == "Remover suspeito":
        nome_remover = input()
        if nome_remover in dicionario_famosos.keys():
            print(f'{nome_remover} removido da lista de suspeitos, está limpo')
            del dicionario_famosos[nome_remover]
        else:
            print("Quem é esse crazy man? Não tá aqui na database")
