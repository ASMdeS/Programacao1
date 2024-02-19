equacao_posfixa = None
equacao_infixa = []
contador_numerico = 0
resposta_final = ""
string_binarios = ""

#Converter notação posfixa em infixa e executar
def conversao_notacao():
    for parte in equacao_posfixa:
        if parte.isdigit():
            equacao_infixa.insert(0, parte)
        else:
            primeiro_operador = equacao_infixa[0]
            equacao_infixa.pop(0)
            segundo_operador = equacao_infixa[0]
            equacao_infixa.pop(0)
            equacao_infixa.insert(0, "(" + segundo_operador + parte + primeiro_operador + ")")
    equacao_final = " ".join(equacao_infixa)
    resultado_final = eval(equacao_final)
    return resultado_final

#Checar se é um número perfeito
def numero_perfeito(resultado_final):
    soma = 0
    for x in range(1, resultado_final):
        if resultado_final % x == 0:
            soma += x
    if soma == resultado_final and resultado_final > 0:
        return 1
    else:
        return 0

#Printar
while equacao_posfixa != ['Todas', 'as', 'expressoes', 'foram', 'enviadas!']:
    equacao_posfixa = input().split()
    equacao_infixa = []
    if equacao_posfixa == []:
        contador_numerico += 1
        print(
            f'''O {contador_numerico}º conjunto de expressoes resultou no binario {string_binarios} que em ASCII eh: {resultado_ascii}
''')
        resposta_final += resultado_ascii
        string_binarios = ""
    elif equacao_posfixa == ['Todas', 'as', 'expressoes', 'foram', 'enviadas!']:
        print(f'''A decodificacao final resultou em:
{resposta_final}''')
    else:
        equacao_infixa = []
        resultado_final = int(conversao_notacao())
        string_binarios += str(numero_perfeito(resultado_final))
        resultado_binario = int(string_binarios, 2)
        resultado_ascii = chr(resultado_binario)