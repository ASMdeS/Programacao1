Arthur = int(input())
Luiz = int(input())
Pedro = int(input())
Tempo = int(input())

x = (Arthur + Luiz + abs((Arthur - Luiz))) / 2
y = (x + Pedro + abs((x - Pedro))) / 2

print(int(y*Tempo))