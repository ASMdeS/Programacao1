class playlist:
    def __init__(self, nome, musicas):
        self.nome = nome
        self.musicas = musicas

    def adicionar(self, musica):
        self.musicas.append(musica)

    def remover(self):
        self.musicas.pop()

    def reproduzir(self):
        print(f'Play em {self.musicas}')
        for elemento in musicas:
            print(f'Tocando {elemento}...')
        print(f'Essa festa foi um sucesso!')

    def duracao(self):
        return (len(musicas) * 3)

lista_generos = []

qtd_playlists = int(input())
print(qtd_playlists)

for i in range(0, qtd_playlists):
    nome = input()
    genero = input()
    musicas = input()
    lista_generos.append(genero)
    genero = playlist(nome, musicas.split(', '))

genero_tocado = input()
duracao_festa = int(input())
for elemento in lista_generos:
    if elemento == genero_tocado:
        if elemento.duracao() < duracao_festa:
            musicas_faltando =

