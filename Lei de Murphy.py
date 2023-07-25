equacao_posfixa = input().split()
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
                equacao_infixa.insert(equacao_posfixa.index(parte) + 1, parte)
                equacao_infixa.insert(equacao_posfixa.index(parte) - 2, '(')
                equacao_infixa.insert(equacao_posfixa.index(parte) + 2, ')')

    print(equacao_infixa)
    equacao_final = " ".join(equacao_infixa)
    print(equacao_final)
    resultado_final = eval(equacao_final)
    print(resultado_final)



conversao_notacao()