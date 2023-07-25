equacao_posfixa = None
equacao_infixa = []

def conversao_notacao():
    for parte in equacao_posfixa:
        print(parte)
        if parte.isdigit():
            equacao_infixa.append(parte)
        else:
            if '(' in equacao_infixa:
                equacao_infixa.insert(equacao_posfixa.index(parte) + 1, parte)
            else:
                equacao_infixa.insert(equacao_posfixa.index(parte) - 1, parte)
                equacao_infixa.insert(equacao_posfixa.index(parte) - 2, '(')
                equacao_infixa.insert(equacao_posfixa.index(parte) + 2, ')')
        print(equacao_infixa)

    print(equacao_infixa)
    equacao_final = " ".join(equacao_infixa)
    print(equacao_final)
    resultado_final = eval(equacao_final)
    print(resultado_final)


def numero_perfeito(resultado_final):
    soma = 0
    for x in range(1, resultado_final):
        if resultado_final % x == 0:
            soma += x
    if soma == resultado_final:
        return 1
    else:
        return 0


while equacao_posfixa != ['Todas', 'as', 'expressoes', 'foram', 'enviadas!']:
    equacao_posfixa = input().split()
    equacao_infixa = []
    conversao_notacao()