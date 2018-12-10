# Função que gera um dicionário a partir do arquivo convidados.

def gerar_dicionario(txt):
    chave = ''
    valor = ''
    cont = 0
    dicionario = dict()

    arquivo = open(txt, 'r')
    convidados = arquivo.read()
    arquivo.close()

    convidados = convidados.replace(" ", "")
    convidados = convidados.replace("#", " ")
    convidados = convidados.replace("--", "\n")
    convidados2 = convidados.split()

    for i in convidados2:
        if cont %2 == 0:
            valor = convidados2[cont]
        else:
            chave = convidados2[cont]
            dicionario[chave] = valor
        cont += 1
    return dicionario
