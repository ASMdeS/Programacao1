quantidade_famosos = int(input())
todos_famosos = dict()

for i in range(0, quantidade_famosos):
    informacoes_famoso = input().split(" - ")
    todos_famosos[informacoes_famoso[0]] = [informacoes_famoso[1], [int(informacoes_famoso[2])]]

todos_famosos = sorted(todos_famosos.items(), key=lambda x:x[1][0])

print(todos_famosos)