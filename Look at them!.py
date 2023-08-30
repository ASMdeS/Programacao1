quantidade_famosos = int(input())
nattys = dict()
fake_nattys = dict()
lista_nattys = []
lista_fakes = []

for i in range(0, quantidade_famosos):
    informacoes_famoso = input().split(" - ")
    if informacoes_famoso[2] == "natty":
        nattys[informacoes_famoso[0]] = [int(informacoes_famoso[1])], [informacoes_famoso[2]]
    else:
        fake_nattys[informacoes_famoso[0]] = [int(informacoes_famoso[1])], [informacoes_famoso[2]]

nattys = sorted(nattys.items(), key=lambda x:x[1][0])
fake_nattys = sorted(fake_nattys.items(), key=lambda x:x[1][0])

print(nattys)
print(fake_nattys)

for natty in range(0, len(nattys)):
    nome = list(nattys[natty].keys())[natty]
    score = nattys[list(nattys.keys())[natty]][0]
    veredito = nattys[list(nattys.keys())[natty]][1]
    tupla_nattys.append(f'{nome} - {score} - {veredito}')

for fake in range(0, len(fake_nattys)):
    nome = list(fake_nattys.keys())[fake]
    score = fake_nattys[list(fake_nattys.keys())[fake]][0]
    veredito = fake[list(fake_nattys.keys())[fake]][1]
    tupla_fakes.append(f'{nome} - {score} - {veredito}')

final = (lista_nattys, lista_fakes)

#Print
print(quantidade_famosos)
for cara in tupla_nattys:
    print(cara)
for pessoa in tupla_fakes:
    print(pessoa)