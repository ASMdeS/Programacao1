Caracteristica1 = input()
Caracteristica2 = input()
Nome = input()
Habilidade = input()
Nota1 = int(input())
Nota2 = int(input())
Nota3 = int(input())
Media = (Nota1 + Nota2 + Nota3) / 3


if Caracteristica1 == "Humildade" and Caracteristica2 == "Bondade":
    if Nome == "Mary" or Nome == "Ninguem":
        if Habilidade == "Dancar" or Habilidade == "Lancar":
            if Media >= 7:
                print("Siga em frente, olhe para o lado. Bem-vindo ao aranhaverso, Miranha Furacao!")
            else:
                print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
                print("Infelizmente você não obteve um bom desempenho escolar!")
        else:
            print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
            print("Infelizmente você não possui as habilidades necessárias!")
    else:
        print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
        print("Infelizmente você não está apaixonado pela pessoa certa!")
else:
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")
    print("Infelizmente você não possui as característica necessárias!")