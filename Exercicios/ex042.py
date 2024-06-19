from random import randint
from time import sleep
from emoji import emojize
op = randint(0,2)
itens = ('Pedra','Papel','Tesoura')
print('=-'*15)
print('GAME PEDRA PAPEL TESOURA')
print('=-'*15)
print('Suas opções: ')
print(emojize('[0] PEDRA :gem_stone:'))
print(emojize('[1] PAPEL :roll_of_paper:'))
print(emojize('[1] TESOURA :scissors:'))
jogo = int(input('Qual é a sua jogada ? '))
sleep(1)
print('\033[1;31mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\033[m')
sleep(1)
print('=-'*15)
print('O PC jogou {}'.format(itens[op]))
print('O usuário jogou {}'.format(itens[jogo]))
print('=-'*15)
if jogo == op:
    print('Empate')
elif jogo == 0 and op == 1:
    print("PC VENCEU")
elif jogo == 0 and op == 2:
    print('PC venceu')
elif jogo == 1 and op == 0:
    print('Usuário venceu')
elif jogo == 1 and op == 2:
    print('PC venceu')
elif jogo == 2 and op == 0:
    print('PC Venceu')
elif jogo == 2 and op == 1:
    print('Usuário venceu')