from time import sleep
c = ('\033[m', # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30;40m'  # 6 - branco 
); # cores do terminal


def ajuda(com): #função que mostra a ajuda
    titulo(f'Acessando o manual do comando \'{com}\' ', 4) #comando que vai ser mostrado 
    print(c[6], end='') 
    help(com) 
    print(c[0], end='') 
    sleep(2)


def titulo(msg, cor=0): # função que mostra o titulo
    tam = len(msg) + 4 # tamanho da mensagem
    print(c[cor], end='') #cor da mensagem
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)


# programa principal
comando = '' # comando vazio para iniciar o programa
while True: # loop infinito
    titulo('SISTEMA DE AJUDA PyHELP', 2) # titulo do programa
    comando = str(input('< Função Bibilioteca > ')) 
    if comando.upper() == 'FIM': # se o comando for fim, o programa para
        break
    else:
        ajuda(comando) # chama a função ajuda
titulo('ATÉ LOGO', 1)