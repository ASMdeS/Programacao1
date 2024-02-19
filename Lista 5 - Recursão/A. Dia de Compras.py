#Começando
str_random = input()
string_minusculas = ""
string_maiusculas = ""
preco = None

#Função Fatorial
def fatorial(numero):
   if numero == 1:
       return numero
   else:
       return numero*fatorial(numero-1)

#Descobrindo quais são as maiusculas e minusculas
for minuscula in str_random:
    if minuscula.islower():
        string_minusculas += minuscula
for maiuscula in str_random:
    if maiuscula.isupper():
        string_maiusculas += maiuscula

#Calculando preco
if len(string_minusculas) == len(string_maiusculas):
    preco = len(str_random)**2
elif len(string_minusculas) > len(string_maiusculas):
    preco = fatorial(len(string_minusculas))*len(str_random)
elif len(string_maiusculas) > len(string_minusculas):
    preco = fatorial(len(string_maiusculas))*len(str_random)

if preco >= 100:
    print(f'Hum... {preco}? Acho que na volta eu compro')
else:
    print(f'{preco}! Vou comprar todos!')