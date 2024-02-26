# Recebendo a entrada
entrada = int(input())

# Criando a soma de divisores
soma_divisores = 0

# Adicionando os divisores
for i in range(1, entrada):
    if entrada % i == 0:
        soma_divisores += i

# Imprimndo caso o número seja perfeito
if soma_divisores == entrada:
    print(f"O número {entrada} é perfeito!")

# Imprimindo caso o número não seja perfeito
else:
    print(f"O número {entrada} não é perfeito!")
