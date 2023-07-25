equacao_posfixa = input().split()

def conversao_notacao():
    for parte in equacao_posfixa:
        equacao_infixa = []
        if parte.isdigit():
            equacao_infixa.append(parte)
        else:
            equacao_infixa.insert(parte.index() - 1, parte)
    print(equacao_infixa)

conversao_notacao()