def comparar(entrada, buscada, index_entrada, index_buscada, frase_entrada, frase_buscada, boolean):
    print(buscada[list(buscada.keys())[frase_buscada]])
    print(entrada[list(entrada.keys())[frase_entrada]])
    if boolean is True:
        print("ddddddddddddddddddddddddddddddddddd")
        print(buscada[list(buscada.keys())[frase_buscada]][index_buscada])
        print(entrada[list(entrada.keys())[frase_entrada]][index_entrada])
        if buscada[list(buscada.keys())[frase_buscada]][index_buscada] == entrada[list(entrada.keys())[frase_entrada]][index_entrada]:
            print(boolean)
            return comparar(entrada, buscada, index_entrada + 1, index_buscada + 1, frase_entrada, frase_buscada, True)
    else:
        print(entrada[list(entrada.keys())[frase_entrada]])
        for trigrama in entrada[list(entrada.keys())[frase_entrada]]:
            print(trigrama)
            print(buscada[list(buscada.keys())[0]][0])
            if buscada[list(buscada.keys())[frase_buscada]][0] == trigrama:
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                return comparar(entrada, buscada, index_entrada, index_buscada + 1, frase_entrada, frase_buscada, True)
    return comparar(entrada, buscada, index_entrada, index_buscada, frase_entrada + 1, frase_buscada, False)