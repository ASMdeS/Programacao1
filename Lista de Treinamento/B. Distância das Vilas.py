A = int(input())
B = int(input())

H = ((A - 34)**2 + (B - 220)**2)**0.5
K = ((A - 0)**2 + (B - 0)**2)**0.5
S = ((A - 140)**2 + (B - 456)**2)**0.5

print(f"Distancia para Hogsmeade: {H:.2f}")
print(f"Distancia para Kakariko: {K:.2f}")
print(f"Distancia para Solitude: {S:.2f}")