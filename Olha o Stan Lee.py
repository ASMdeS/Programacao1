caracteres = int(input())
filme_1 = input()
filme_2 = input()
filme_3 = input()

cansaco = 0

if filme_1 == "Coringa" or filme_1 == "Batman vs Superman" or filme_1 == "O Cavaleiro das Trevas":
    print("Algo de errado não está certo!")
    exit()

if (caracteres % 2) == 0:
    dica = ((caracteres/2) ** 0.5) + 2
else:
    dica = (caracteres/3) + 3

if filme_1 == "Vingadores: Ultimato":
    cansaco = cansaco + 2
else:
    cansaco = cansaco + 1

if len(filme_1) == dica:
    print("Miles: Achei o easter egg!!!")
    filme_4 = input()
    duracao = int(input())
    if duracao >= 135 and cansaco >= 2:
        print("Miles: A mimir")
    elif duracao >= 120 and cansaco >= 2:
        print("Gwen: Nada que uma xícara de café não resolva!")
    else:
        print("Peter: " + filme_4 + " é o melhor filme do homem aranha, 10/10")
else:
    print("Miles: Tou frio, melhor ir procurar nas fases mais antigas")
    if filme_2 == "Vingadores: Ultimato":
        cansaco = cansaco + 2
    else:
        cansaco = cansaco + 1
if len(filme_2) == dica:
    print("Miles: Achei o easter egg!!!")
    filme_4 = input()
    duracao = int(input())
    if duracao >= 135 and cansaco >= 2:
        print("Miles: A mimir")
    elif duracao >= 120 and cansaco >= 2:
        print("Gwen: Nada que uma xícara de café não resolva!")
    else:
        print("Peter: " + filme_4 + " é o melhor filme do homem aranha, 10/10")
else:
    if len(filme_1) != dica:
        print("Gwen: Cadê o velho??? Queria um autógrafo")
    if filme_3 == "Vingadores: Ultimato":
        cansaco = cansaco + 2
    else:
        cansaco = cansaco + 1
if len(filme_3) == dica:
    print("Miles: Achei o easter egg!!!")
    filme_4 = input()
    duracao = int(input())
    if duracao >= 135 and cansaco >= 2:
        print("Miles: A mimir")
    elif duracao >= 120 and cansaco >= 2:
        print("Gwen: Nada que uma xícara de café não resolva!")
    else:
        print("Peter: " + filme_4 + " é o melhor filme do homem aranha, 10/10")
if len(filme_1) != dica and len(filme_2) != dica and len(filme_3) != dica:
    print("Peter: Parece que o próximo filme do aranha-verso vai demorar mais do que esperado pra sair...")
