from random import randint
from time import sleep
print("=-"*15)
print('\033[1;33mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print("=-"*15) 
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0,11)
    s = pc + jogador
    if s % 2 == 0:
        cont = cont + 1
        print('-'*35)
        print(f'Você jogou {jogador} e o computador jogou {pc}. Total {jogador + pc}')
        print('-'*35)
        print('Você VENCEU') 
        print('Vamos Jogar Novamente...')
        print('=-'*20)
        sleep(2)
    else:
        print('-'*35)
        print(f'Você jogou {jogador} e o computador jogou {pc}. Total {jogador + pc}') 
        print('-'*35)
        print('Você PERDEU')
    if s % 2 != 0:
        break 
print('=-'*20)
print(f'Você venceu {cont} vezes')
print('=-'*20)

