primeira = input()
primeira_ponto = int(input())

segunda = input()
segunda_ponto = int(input())

terceira = input()
terceira_ponto = int(input())

quarta = input()
quarta_ponto = int(input())

quinta = input()
quinta_ponto = int(input())

dois = primeira_ponto + segunda_ponto
tres = primeira_ponto + segunda_ponto + terceira_ponto
quatro = primeira_ponto + segunda_ponto + terceira_ponto + quarta_ponto
total = primeira_ponto + segunda_ponto + terceira_ponto + quarta_ponto + quinta_ponto
todo = str(total)



if primeira == "novo lançador de teias" and segunda != "NADA":
    print("Com calma, aranha")
    if segunda == "lentes de visão avançada":
        print("Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro")
        if terceira == "traje à prova de balas":
            print("UOU, só tente sair dessa vivo, vou otimizar a energia aqui")

if primeira == "ativação de inteligência artificial" or segunda == "ativação de inteligência artificial" or terceira == "ativação de inteligência artificial" or quarta == "ativação de inteligência artificial" or quinta == "ativação de inteligência artificial":
    print("Espero que não esteja ativando isso para usar nas provas")
    if primeira == "novo lançador de teias" or segunda == "novo lançador de teias" or terceira == "novo lançador de teias" or quarta == "novo lançador de teias" or quinta == "novo lançador de teias":
        if primeira == "membranas planadoras" or segunda == "membranas planadoras" or terceira == "membranas planadoras" or quarta == "membranas planadoras" or quinta == "membranas planadoras":
            if tres >=80 or quatro >=80 or total >= 80:
                print("Vou descarregar em questão de minutos, pare AGORA")
                print("Tudo certo, mas cuidado ao ficar conversando com IA enquanto voa")
            else:
                print("Vou descarregar em questão de minutos, pare AGORA")



print("Aranha, nessa sequência você usou " + todo + " de energia!")

