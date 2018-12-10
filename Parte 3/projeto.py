'''
O arquivo pdf gerado deverá ser enviado por e-mail
'''

from funcoes import *

comando = input('Deseja gerar um dicionário a partir de um arquivo?\n\n S/N\n\n')

if comando == 's' or comando == 'S':
    nome_arquivo = input('\nDigite o nome do arquivo: ')
    while nome_arquivo != 'convidados.txt':
        nome_arquivo = input('\nArquivo inválido, digite novamente o nome do arquivo: ')
    dicio = gerar_dicionario(nome_arquivo)
    print('\nDicionário gerado:')
    print(dicio)

    comando = input('\nDeseja gerar um PDF com o dicionário?\n\n S/N\n\n')
    if comando == 's' or comando == 'S':
        gerar_pdf(dicio)
        comando = input('\nDeseja enviar o PDF gerado por e-mail?\n\n S/N\n\n')
        if comando == 's' or comando == 'S':
            de = input('\nQual o remetente? ')
            para = input('\nQual o destinatário? ')
            senha = input('\nDigite sua senha: ')
            enviar_email(de, para, senha)
        else:
            print('Fechando o programa.')
    else:
        print('Fechando o programa.')
