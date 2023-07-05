time = 0
pontos = 0
nome = None
Top = None
Jungler = None
Mid = None
Adc = None
Suporte = None
Vitoria = True
Artur = False
Frej = False
primeiro = None
segundo = None
terceiro = None
quarto = None
quinto = None

while time < 5 and nome != "Bruna":
    nome = input()
    #Checar se o nome é Bruna
    if nome == "Bruna":
        print("LOL NÃO!!! TUDO MENOS LOL!!!")
    else:
        lane = input()
        elo = input()

        if elo != "Bronze" and elo != "Prata" and elo != "Ouro" and elo != "Platina" and elo != "Diamante" and elo != "Desafiante":
            print("Não conheço esse elo, então vou considerar que é um elo ruim.")

        #Lane

        if lane == "Top":
            if Top is None:
                Top = nome + " - " + lane + " (" + elo + ")"
                print(nome + " entrou pro time.")
                if time == 0:
                    primeiro = Top
                if time == 1:
                    segundo = Top
                if time == 3:
                    terceiro = Top
                if time == 3:
                    quarto = Top
                if time == 4:
                    quinto = Top
                time = time + 1
                if elo == "Bronze":
                    pontos = pontos + 1
                elif elo == "Prata":
                    pontos = pontos + 2
                elif elo == "Ouro":
                    pontos = pontos + 4
                elif elo == "Platina":
                    pontos = pontos + 6
                elif elo == "Diamante":
                    pontos = pontos + 8
                elif elo == "Desafiante":
                    pontos = pontos + 10
            else:
                print(nome + " não foi aceito, que pena.")

        if lane == "Jungler":
            if Jungler is None:
                Jungler = nome + " - " + lane + " (" + elo + ")"
                print(nome + " entrou pro time.")
                if time == 0:
                    primeiro = Jungler
                if time == 1:
                    segundo = Jungler
                if time == 2:
                    terceiro = Jungler
                if time == 3:
                    quarto = Jungler
                if time == 4:
                    quinto = Jungler
                time = time + 1
                if elo == "Bronze":
                    pontos = pontos + 1
                elif elo == "Prata":
                    pontos = pontos + 2
                elif elo == "Ouro":
                    pontos = pontos + 4
                elif elo == "Platina":
                    pontos = pontos + 6
                elif elo == "Diamante":
                    pontos = pontos + 8
                elif elo == "Desafiante":
                    pontos = pontos + 10
            else:
                print(nome + " não foi aceito, que pena.")
        if lane == "Mid":
            if Mid is None:
                Mid = nome + " - " + lane + " (" + elo + ")"
                print(nome + " entrou pro time.")
                if time == 0:
                    primeiro = Mid
                if time == 1:
                    segundo = Mid
                if time == 2:
                    terceiro = Mid
                if time == 3:
                    quarto = Mid
                if time == 4:
                    quinto = Mid
                time = time + 1
                if elo == "Bronze":
                    pontos = pontos + 1
                elif elo == "Prata":
                    pontos = pontos + 2
                elif elo == "Ouro":
                    pontos = pontos + 4
                elif elo == "Platina":
                    pontos = pontos + 6
                elif elo == "Diamante":
                    pontos = pontos + 8
                elif elo == "Desafiante":
                    pontos = pontos + 10
            else:
                print(nome + " não foi aceito, que pena.")

        if lane == "Adc":
            if Adc is None:
                Adc = nome + " - " + lane + " (" + elo + ")"
                print(nome + " entrou pro time.")
                if time == 0:
                    primeiro = Adc
                if time == 1:
                    segundo = Adc
                if time == 2:
                    terceiro = Adc
                if time == 3:
                    quarto = Adc
                if time == 4:
                    quinto = Adc
                time = time + 1
                if elo == "Bronze":
                    pontos = pontos + 1
                elif elo == "Prata":
                    pontos = pontos + 2
                elif elo == "Ouro":
                    pontos = pontos + 4
                elif elo == "Platina":
                    pontos = pontos + 6
                elif elo == "Diamante":
                    pontos = pontos + 8
                elif elo == "Desafiante":
                    pontos = pontos + 10
            else:
                print(nome + " não foi aceito, que pena.")

        if lane == "Suporte":
            if Suporte is None:
                Suporte = nome + " - " + lane + " (" + elo + ")"
                print(nome + " entrou pro time.")
                if time == 0:
                    primeiro = Suporte
                if time == 1:
                    segundo = Suporte
                if time == 2:
                    terceiro = Suporte
                if time == 3:
                    quarto = Suporte
                if time == 4:
                    quinto = Suporte
                time = time + 1
                if elo == "Bronze":
                    pontos = pontos + 1
                elif elo == "Prata":
                    pontos = pontos + 2
                elif elo == "Ouro":
                    pontos = pontos + 4
                elif elo == "Platina":
                    pontos = pontos + 6
                elif elo == "Diamante":
                    pontos = pontos + 8
                elif elo == "Desafiante":
                    pontos = pontos + 10
            else:
                print(nome + " não foi aceito, que pena.")

        #Nomes

        if nome == "Artur":
            print("Ele tá meio enferrujado...")
            Artur = True
        elif nome == "Frej":
            print("Joga muito!")
            Frej = True

        if time == 5 and nome != "Bruna":
            print("O time está completo.")
            print(primeiro)
            print(segundo)
            print(terceiro)
            print(quarto)
            print(quinto)
            if Artur == True and Frej == False:
                print("Vai dar ruim...")
            elif Artur == False and Frej == True:
                print("A GENTE VAI GANHAR!!!")
            else:
                if pontos >= 18:
                    print("A GENTE VAI GANHAR!!!")
                else:
                    print("Vai dar ruim...")