#O que será usado no código
quantidade_famosos = int(input())
nattys = dict()
fake_nattys = dict()
lista_print = []

#Formar o dicionário dos famosos fake e o dos nattys
for i in range(0, quantidade_famosos):
    informacoes_famoso = input().split(" - ")
    if informacoes_famoso[2] == "natty":
        nattys[informacoes_famoso[0]] = [int(informacoes_famoso[1])], [informacoes_famoso[2]]
    else:
        fake_nattys[informacoes_famoso[0]] = [int(informacoes_famoso[1])], [informacoes_famoso[2]]

#Ordenar os dicionários, criando uma lista de tuplas
tupla_nattys = sorted(nattys.items(), key=lambda x:x[1][0], reverse=True)
tupla_fakes = sorted(fake_nattys.items(), key=lambda x:x[1][0], reverse=True)

#Criar uma lista com os nomes,score e veredito segundo o padrão nome - score - veredito
for natty in tupla_nattys:
    lista_print.append(f'{natty[0]} - {natty[1][0][0]} - {natty[1][1][0]}')
for fake in tupla_fakes:
    lista_print.append(f'{fake[0]} - {fake[1][0][0]} - {fake[1][1][0]}')

#Printar
for famoso in lista_print:
    print(famoso)