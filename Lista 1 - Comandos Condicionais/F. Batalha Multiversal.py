nomeAranha = input()

ataqueAranha = int(input())

defesaAranha = int(input())

nomeAliado = input()

ataqueAliado = int(input())

defesaAliado = int(input())

nomeVilao = input()

ataqueVilao = int(input())

defesaVilao = int(input())

nomeCapanga = input()

ataqueCapanga = int(input())

defesaCapanga = int(input())

Sorte1 = int(input())

Sorte2 = int(input())

Sorte3 = int(input())

contagem = 0

print("1° confronto:")

if Sorte1 == 0:
    if ataqueAranha >= defesaVilao:
        print("O " + nomeAranha + " acertou vários golpes no " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeVilao + " está dificultando a vida do " + nomeAranha)
elif Sorte1 == 1:
    if ataqueAranha + ataqueAliado >= defesaVilao:
        print("O " + nomeAranha + " acertou vários golpes no " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeVilao + " está dificultando a vida do " + nomeAranha)
elif Sorte1 == 2:
    if ataqueAranha > defesaVilao + defesaCapanga:
        print("O " + nomeAranha + " acertou vários golpes no " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeVilao + " está dificultando a vida do " + nomeAranha)
elif Sorte1 == 3:
    if ataqueAranha + ataqueAliado >= defesaVilao + defesaCapanga:
        print("O " + nomeAranha + " acertou vários golpes no " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeVilao + " está dificultando a vida do " + nomeAranha)

print("2° confronto:")

if Sorte2 == 0:
    if defesaAranha >= ataqueVilao:
        print("O " + nomeAranha + " contra-atacou o " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeAranha + " não consegue se defender contra o " + nomeVilao)
elif Sorte2 == 1:
    if defesaAranha > ataqueVilao + ataqueCapanga:
        print("O " + nomeAranha + " contra-atacou o " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeAranha + " não consegue se defender contra o " + nomeVilao)

elif Sorte2 == 2:
    if defesaAranha + defesaAliado >= ataqueVilao:
        print("O " + nomeAranha + " contra-atacou o " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeAranha + " não consegue se defender contra o " + nomeVilao)
elif Sorte2 == 3:
    if defesaAranha + defesaAliado >= ataqueVilao + ataqueCapanga:
        print("O " + nomeAranha + " contra-atacou o " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeAranha + " não consegue se defender contra o " + nomeVilao)

print("3° confronto:")

if Sorte3 == 0:
    if ataqueAranha >= defesaVilao:
        print("O " + nomeAranha + " acertou vários golpes no " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeVilao + " está dificultando a vida do " + nomeAranha)
elif Sorte3 == 1:
    if ataqueAranha + ataqueAliado >= defesaVilao:
        print("O " + nomeAranha + " acertou vários golpes no " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeVilao + " está dificultando a vida do " + nomeAranha)
elif Sorte3 == 2:
    if ataqueAranha > defesaVilao + defesaCapanga:
        print("O " + nomeAranha + " acertou vários golpes no " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeVilao + " está dificultando a vida do " + nomeAranha)
elif Sorte3 == 3:
    if ataqueAranha + ataqueAliado >= defesaVilao + defesaCapanga:
        print("O " + nomeAranha + " acertou vários golpes no " + nomeVilao)
        contagem = contagem + 1
    else:
        print("O " + nomeVilao + " está dificultando a vida do " + nomeAranha)

if contagem >= 2:
    print("O " + nomeAranha + " e " + nomeAliado + " conseguiram derrotar o " + nomeVilao + " e recuperar o multiverso!")