class Personagem:
    def __init__(self, aneis_coletados, esmeraldas_coletadas, escudo_equipado, sonic_morto, super_sonic):
        self.aneis_coletados = aneis_coletados
        self.esmeraldas_coletadas = esmeraldas_coletadas
        self.escudo_equipado = escudo_equipado
        self.sonic_morto = sonic_morto
        self.super_sonic = super_sonic

    def adicionar_aneis(self, quantidade_aneis):
        self.aneis_coletados += quantidade_aneis

    def equipar_escudo(self):
        self.escudo_equipado = True

    def adicionar_esmeralda(self):
        self.esmeraldas_coletadas += 1

    def sofrer_dano(self):
        if self.escudo_equipado:
            self.escudo_equipado = False
        elif self.aneis_coletados > 0:
            self.aneis_coletados = 0
        else:
            self.sonic_morto = True


sonic = Personagem(0, 0, False, False, False)

while sonic.sonic_morto is False and (sonic.aneis_coletados < 50 or sonic.esmeraldas_coletadas < 7):
    entrada = input()
    if entrada == "aneis":
        quantidade_aneis = int(input())
        sonic.adicionar_aneis(quantidade_aneis)
        print(f'Sonic esta agora com {sonic.aneis_coletados} aneis! Gotta go fast!!!')
    elif entrada == "escudo":
        if sonic.escudo_equipado:
            print(f'Sonic ja esta equipado com uma protecao extra!!!')
        else:
            sonic.equipar_escudo()
            print("Sonic esta agora com uma camada a mais de protecao!!! Let's go!!!")
    elif entrada == "dano":
        sonic.sofrer_dano()
        print("Maldito robo do Eggman!!! Este sera seu fim, bigodudo!!!")
    elif entrada == "esmeralda":
        if sonic.esmeraldas_coletadas < 6:
            sonic.adicionar_esmeralda()
            print(f'Sonic ainda precisa encontrar mais {7 - sonic.esmeraldas_coletadas} esmeraldas!!!')
        elif sonic.esmeraldas_coletadas == 6:
            sonic.adicionar_esmeralda()
            print("Sonic acabou de encontrar a esmeralda que faltava!!!")
        else:
            print("Sonic ja possui todas as esmeraldas!!!")
    if sonic.sonic_morto:
        print("Infelizmente, nosso heroi nao conseguiu correr o bastante para derrotar seu nemesis...")
    if sonic.aneis_coletados >= 50 and sonic.esmeraldas_coletadas >= 7:
        print("Com o poder das esmeraldas do caos, Super Sonic conseguiu deter os planos malignos do Dr. Robotinik!!!")
