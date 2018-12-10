from reportlab.pdfgen import canvas

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

#Função que gera o PDF:

def gerar_pdf(dicionario):
    doc = canvas.Canvas('contatos.pdf')
    print('\nArquivo contatos.pdf criado com sucesso.')

    coluna = 80
    linha = 800

    doc.drawString(coluna, linha, 'Nomes e telefones:')

    for numero, contato in dicionario.items():
        linha -= 15
        doc.drawString(coluna, linha, contato + ':' + numero)

    doc.save()
    print('\nArquivo contatos.pdf salvo com sucesso.')
