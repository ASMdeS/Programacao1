# Função Fatorial
def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)


# Recebendo a entrada
entrada = int(input())

# Imprimindo o fatorial
print(fatorial(entrada))
