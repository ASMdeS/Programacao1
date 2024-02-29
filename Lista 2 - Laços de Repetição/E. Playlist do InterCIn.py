# Meta diaria
meta_diaria = 10

# Recebendo a duracao da playlist
duracao_playlist = int(input())

# For Loop para receber as musicas e imprimir conforme o desejado
for dia in range(0, 3):
    if duracao_playlist > 0:
        animacao_torcida = 0
        num_musicas_tocadas_dias = int(input())
        musica_mais_animada = None
        indice_musica_mais_animada = 0
        for i in range(0, num_musicas_tocadas_dias):
            nome_musica = input()
            duracao_musica_segundos = int(input())
            indice_animacao_musica = int(input())
            animacao_torcida += int(indice_animacao_musica * 0.8)
            duracao_playlist -= duracao_musica_segundos
            if indice_animacao_musica > indice_musica_mais_animada:
                musica_mais_animada = nome_musica
                indice_musica_mais_animada = indice_animacao_musica
        print(f'Dia {dia + 1} do InterCIn')
        print(f'A música mais animada do dia foi {musica_mais_animada}')
        if animacao_torcida >= meta_diaria:
            meta_diaria = 10
        if dia < 2 and animacao_torcida < meta_diaria:
            meta_diaria += 10
            meta_diaria -= animacao_torcida
            print(
                f'Mesmo assim, não foi o suficiente para deixar o pessoal animado. Serão necessários pelo menos {meta_diaria} pontos de animação no outro dia')
        if dia == 2 and duracao_playlist > 0:
            if animacao_torcida < meta_diaria:
                print("Valeu a tentativa, na próxima vai dar bom")
                print("A playlist estava boa, mas não foi o suficiente para animar o evento")
            else:
                print("A playlist estava incrível demais!")
        if duracao_playlist <= 0:
            print("Estava animado, mas a playlist acabou antes do evento terminar e todo mundo ficou muito triste :(")
