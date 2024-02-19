class playlist:
    def __init__(self, nome, genero, musicas):
        self.nome = nome
        self.genero = genero
        self.musicas = musicas

    def adicionar(self, musica):
        self.musicas.append(musica)

    def remover(self):
        self.musicas.pop()

    def reproduzir(self):
        print(f'Play em {self.nome}')
        for elemento in self.musicas:
            print(f'Tocando {elemento}...')
        print(f'Essa festa foi um sucesso!')

    def duracao(self):
        return (len(self.musicas) * 3)


def ajustar_playlist():
    duracao_atual = playlist_obj.duracao()
    print(duracao_atual)
    musicas_adicionadas = 0
    musicas_removidas = 0

    while duracao_atual > duracao_festa + 2:
        playlist_obj.remover()
        duracao_atual = playlist_obj.duracao()
        musicas_removidas += 1

    while duracao_atual + 2 < duracao_festa:
        duracao_atual += 3
        musicas_adicionadas += 1

    return musicas_adicionadas, musicas_removidas


def correcao_playlist(musicas_faltando, musicas_sobrando):
    if musicas_faltando > 0:
        print(f'Precisaremos adicionar mais {musicas_faltando} músicas a playlist {playlist_obj.nome}')
        for i in range(musicas_faltando):
            musica = input()
            playlist_obj.musicas.append(musica)
    if musicas_sobrando > 0:
        print(f'Precisaremos remover {musicas_sobrando} músicas da playlist {playlist_obj.nome}')


# Crie uma lista de playlists
lista_playlists = []
lista_generos = []

qtd_playlists = int(input())

for i in range(0, qtd_playlists):
    nome = input()
    genero = input()
    musicas = input().split(', ')
    playlist_obj = playlist(nome, genero, musicas)
    lista_playlists.append(playlist_obj)

genero_tocado = input()
duracao_festa = int(input())
encontrou_playlist = False

for i, playlist_obj in enumerate(lista_playlists):
    if playlist_obj.genero == genero_tocado:
        musicas_faltando, musicas_sobrando = ajustar_playlist()
        correcao_playlist(musicas_faltando, musicas_sobrando)
        playlist_obj.reproduzir()
        encontrou_playlist = True

if not encontrou_playlist:
    print(f'Não tenho nenhuma playlist do gênero {genero_tocado}, infelizmente não poderei tocar')
