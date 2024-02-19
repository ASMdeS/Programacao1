Dias = int(input())
Casas = int(input())

HorasVida = Dias * 3
DiasJogo = HorasVida * 3
Ticks = DiasJogo * 24000

print(int(Ticks/Casas/2))