# crie um sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo
# de texto simples.
# o sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas

import cadastro
import manarquivo

arquivo = 'pessoas.txt'
if not manarquivo.verificaArquivo(arquivo):
    manarquivo.criarArquivo(arquivo)


cadastro.menu(arquivo)

