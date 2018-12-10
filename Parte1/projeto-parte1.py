'''
Fazer uma análise no arquivo convidados.txt, verificando seu conteúdo, como as
informações estão separadas e organizadas. Em seguida, é necessário coletar todos os dados e
organizar em um dicionário contendo apenas as seguintes informações telefone como chave e
nome como valor. Deverá ser feita uma função que receba uma o caminho/nome do arquivo e
que retorne o dicionário.
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
else:
    print('Fechando o programa.')
