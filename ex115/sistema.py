from cursoemvideo.ex115.lib.interface import *
from cursoemvideo.ex115.lib.arquivo import * #Esse import * é para importar tudo
from time import sleep

arq = 'cursoemvideo.txt' #Nome do meu arquivo txt que será criado

if not arquivoExiste(arq): #Se não existir o arquivo então cria um arquivo novo
    CriarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        #Opção de listar um conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção para cadastrar pessoas
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Até Logo!')
        break #Para encerrar o programa
    else:
        print('\033[31m ERRO! Digite uma opção válida \033[m')
    sleep(1)