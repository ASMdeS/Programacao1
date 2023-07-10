numero = int(input())
lista = []

for i in range(0, numero):
    animal = input()
    if animal in lista:
        print("Criatura repetida")
    else:
        lista.append(animal)

print("Registradas:")
for i in range(0, len(lista)):
    print(lista[i])