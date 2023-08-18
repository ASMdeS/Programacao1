quantidade_famosos = int(input())
todos_famosos = dict()
colecao_famoso = dict()

for n in range(0, quantidade_famosos):
    lista_famosos = input().split(" - ")
    colecao_famoso['nome_famoso'] = lista_famosos[0]
    colecao_famoso['profissao'] = lista_famosos[1]
    colecao_famoso['avaliação_famoso'] = lista_famosos[2]
    colecao_famoso['mês_planejado'] = lista_famosos[3]
    todos_famosos.update(colecao_famoso)
    print(todos_famosos)

print(todos_famosos)