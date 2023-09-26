class Lutador:
    def __init__(self, nome, poder_luta, especie, incluido):
        self.nome = nome
        self.poder_luta = poder_luta
        self.especie = especie
        self.incluido = incluido
        self.adversarios_vencidos = []

    def aumentar_poder(self):
        if self.especie == "Saiyajin":
            self.poder_luta += (self.poder_luta / 10)
        elif self.especie == "Hibrido-Saiyajin":
            self.poder_luta += (self.poder_luta / 5)


contagem_lutadores = 0
lista_objetos = []
total_poder = 0

while contagem_lutadores < 8:
    entrada = input().split()
    if entrada[0] == "ADD":
        lutador_repetido = False
        entrada[1] = Lutador(' '.join(entrada[1:-2]), int(entrada[-2]), entrada[-1], True)
        for elemento in lista_objetos:
            if elemento.nome == entrada[1].nome:
                print(f'{entrada[1].nome} já está no torneio e não pode ser adicionado.')
                lutador_repetido = True
        if lutador_repetido == False:
            contagem_lutadores += 1
            lista_objetos.append(entrada[1])
            if contagem_lutadores == 1:
                print(f'{entrada[1].nome} foi o primeiro a entrar no torneio e aguarda os outros competidores.')
            else:
                if entrada[1].poder_luta > media_poder:
                    print(
                        f'Adversários se preparem!! {entrada[1].nome} está no Torneio e é um dos maiores favoritos a conquistar.')
                else:
                    print(f'{entrada[1].nome} acabou de entrar no torneio, mas acho que não vai muito longe.')

    elif entrada[0] == "DEL":
        removeu_lutador = False
        for elemento in lista_objetos:
            if elemento.nome == entrada[1]:
                lista_objetos.remove(elemento)
                print(f'Infelizmente {elemento.nome} saiu do Torneio.')
                removeu_lutador = True
                contagem_lutadores -= 1
        if removeu_lutador == False:
            print(f'{entrada[1]} ainda não está no Torneio para ser removido.')
    total_poder = 0
    for elemento in lista_objetos:
        total_poder += elemento.poder_luta
        media_poder = total_poder / contagem_lutadores

lista_objetos = sorted(lista_objetos, key=lambda x: x.nome)

primeira_chave = lista_objetos[0:4]
segunda_chave = lista_objetos[4:8]
lista_semifinalistas = []
final = []

# Quartas
print(f'''
### QUARTAS DE FINAL ###''')
for i in range(0, 4):
    if primeira_chave[i].poder_luta > segunda_chave[i].poder_luta:
        primeira_chave[i].aumentar_poder()
        lista_semifinalistas.append(primeira_chave[i])
        print(f'{primeira_chave[i].nome} numa dura batalha vence {segunda_chave[i].nome}.')
        primeira_chave[i].adversarios_vencidos.append(segunda_chave[i].nome)

    else:
        segunda_chave[i].aumentar_poder()
        lista_semifinalistas.append(segunda_chave[i])
        print(f'{segunda_chave[i].nome} numa dura batalha vence {primeira_chave[i].nome}.')
        segunda_chave[i].adversarios_vencidos.append(primeira_chave[i].nome)

lista_semifinalistas = sorted(lista_semifinalistas, key=lambda x: x.nome)
primeiras_semis = lista_semifinalistas[0:2]
segundas_semis = lista_semifinalistas[2:4]

# SEMIS

print(f'''
### SEMI-FINAL ###''')

for i in range(0, 2):
    if primeiras_semis[i].poder_luta > segundas_semis[i].poder_luta:
        primeiras_semis[i].aumentar_poder()
        final.append(primeiras_semis[i])
        print(f'{primeiras_semis[i].nome} numa dura batalha vence {segundas_semis[i].nome}.')
        primeiras_semis[i].adversarios_vencidos.append(segundas_semis[i].nome)

    else:
        segundas_semis[i].aumentar_poder()
        final.append(segundas_semis[i])
        print(f'{segundas_semis[i].nome} numa dura batalha vence {primeiras_semis[i].nome}.')
        segundas_semis[i].adversarios_vencidos.append(primeiras_semis[i].nome)

# FINAL

print(f'''
### FINAL ###''')

if final[0].poder_luta > final[1].poder_luta:
    final[0].aumentar_poder()
    final[0].adversarios_vencidos.append(final[1].nome)
    print(f'{final[0].nome} numa dura batalha vence {final[1].nome}.')
    print(f'''
{final[0].nome}, venceu o Torneio do Poder passando pelos adversários {', '.join(map(str, (final[0].adversarios_vencidos)))} com um poder de luta incrível de {int(final[0].poder_luta)}.''')
else:
    final[1].aumentar_poder()
    final[1].adversarios_vencidos.append(final[0].nome)
    print(f'{final[1].nome} numa dura batalha vence {final[0].nome}.')
    print(f'''
{final[1].nome}, venceu o Torneio do Poder passando pelos adversários {', '.join(map(str, (final[1].adversarios_vencidos)))} com um poder de luta incrível de {int(final[1].poder_luta)}.''')
