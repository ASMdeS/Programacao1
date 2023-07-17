#Listas de itens usados pela Barbie por profissão
itens_medica = ["Estetoscopio", "Esfigmomanometro", "Jaleco", "Caneta" , "Celular"]
itens_informatica = ["Calculadora", "Oculos", "Notebook", "Camisa Social", "Caderno"]
itens_padeira = ["Rolo", "Caneta", "Avental", "Colher de Pau", "Caderno"]
itens_economista = ["Calculadora", "Caneta", "Camisa Social", "Agenda", "Celular"]
itens_personal = ["Halter", "Agenda", "Celular", "Legging", "Corda"]

#Itens da profissão inicial
profissao_inicial = input()
itens_saida = []
if profissao_inicial == "Medica":
    itens_saida = itens_medica.copy()
if profissao_inicial == "Assistente de Informatica":
    itens_saida = itens_informatica.copy()
if profissao_inicial == "Padeira":
    itens_saida = itens_padeira.copy()
if profissao_inicial == "Economista":
    itens_saida = itens_economista.copy()
if profissao_inicial == "Personal Trainer":
    itens_saida = itens_personal.copy()

#Itens da segunda profissão
profissao_segunda = input()
itens_desejados = []
if profissao_segunda == "Medica":
    itens_desejados = itens_medica.copy()
if profissao_segunda == "Assistente de Informatica":
    itens_desejados = itens_informatica.copy()
if profissao_segunda == "Padeira":
    itens_desejados = itens_padeira.copy()
if profissao_segunda == "Economista":
    itens_desejados = itens_economista.copy()
if profissao_segunda == "Personal Trainer":
    itens_desejados = itens_personal.copy()

#Bolsa da Barbie
itens_bolsa = itens_saida.copy()

Saida = False
while Saida == False:
    acao_barbie = input()
    if acao_barbie != "Sair":
        item_barbie = input()
        if acao_barbie == "Adicionar":
            if item_barbie in itens_bolsa:
                print(f"Barbie, você já colocou {item_barbie} na bolsa")
            elif item_barbie in itens_desejados:
                print(f"{item_barbie} adicionado à bolsa")
                itens_bolsa.append(item_barbie)
            else:
                print(f"Barbie, {item_barbie} não esta na lista de itens de {profissao_segunda}")
        elif acao_barbie == "Retirar":
            if item_barbie not in itens_bolsa:
                print(f"Barbie, como você vai retirar algo que já não esta ai?")
            elif item_barbie in itens_desejados:
                print(f"Não faca isso Barbie, você precisa de {item_barbie} para trabalhar de {profissao_segunda}")
            else:
                print(f"{item_barbie} retirado da bolsa")
                itens_bolsa.remove(item_barbie)
    else:
        itens_saida_organizado = sorted(itens_saida)
        itens_desejados_organizado = sorted(itens_desejados)
        itens_bolsa_organizado = sorted(itens_bolsa)
        adicional_listas = [elemento for elemento in itens_bolsa_organizado if elemento not in itens_desejados_organizado]
        diferenca_listas = [elemento for elemento in itens_desejados_organizado if elemento not in itens_bolsa_organizado]

        print(f"Itens na bolsa:", ", ".join(itens_bolsa_organizado))
        if itens_bolsa_organizado == itens_desejados_organizado:
            print("Boa Barbie, foi na correria mas tudo deu certo!")
        elif len(diferenca_listas) > 0:
            print("Oh não!! Barbie, você esqueceu de pegar " + ", ".join(diferenca_listas) + "!!")
        elif len(adicional_listas) > 0:
            print("Barbie, você esqueceu de tirar " + ", ".join(adicional_listas) + ", você não usa ele trabalhando de " + profissao_segunda)

        Saida = True