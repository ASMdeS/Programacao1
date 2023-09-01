#Construir Dicionário
quantidade_famosos = int(input())
colecao_famoso = dict()

for n in range(0, quantidade_famosos):
    lista_famosos = input().split(" - ")
    lista_famosos[1] = lista_famosos[1].split()
    colecao_famoso[lista_famosos[0]] = lista_famosos[1]

#Achar fake natties
mes_selecionado = input()
fake_nattys = []

#Construir lista fake_natties
for i in range(0, len(colecao_famoso)):
    if colecao_famoso[list(colecao_famoso.keys())[i]][2] == mes_selecionado:
        if colecao_famoso[list(colecao_famoso.keys())[i]][1] == 'fake':
            nome = list(colecao_famoso.keys())[i]
            profissao = colecao_famoso[list(colecao_famoso.keys())[i]][0]
            fake_nattys.append(f'{nome} - {profissao}')

#Printar
if len(fake_nattys) > 0:
    print(f'Os fake nattys do mês são:')
    for element in sorted(fake_nattys):
        print(element)
else:
    print(f'Até agora não temos ninguém pra expor na internet neste mês :(')
