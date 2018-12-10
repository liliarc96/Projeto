import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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

# Função de enviar e-mail:

def enviar_email(fromaddr, toaddr, password):
    fromaddr = "liliarc96@gmail.com"
    toaddr = "app.p1.unipe@gmail.com"

    msg = MIMEMultipart()

    msg['De: '] = fromaddr
    msg['Para: '] = toaddr
    msg['Assunto: '] = "Contatos – Aluno"

    body = "Segue os contatos em anexo."

    msg.attach(MIMEText(body, 'plain'))

    filename = "contatos.pdf"
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
