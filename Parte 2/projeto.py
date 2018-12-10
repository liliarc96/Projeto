'''
O dicionário resultante da Parte 1 deverá ser usado para gerar um pdf
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
