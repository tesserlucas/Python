from random import randint
from time import sleep
pc = randint(0, 10) #Faz o pc pensar em um número de 0 a 5
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print('PROCESSANDO...')
sleep(2) #comando usado para o tempo que ele vai ficar processando o print acima
print('-=-' * 10)
jogador = int(input('Em que número eu pensei ? ')) #Jogador tenta advinhar
if jogador < pc:
    print('Mais...Tente mais uma vez')
else:
    print('Menos...Tente mais uma vez')
palpites = 1
while pc != jogador:
    jogador = int(input('Em que número eu pensei ? '))
    palpites = palpites + 1 #para dizer o número de palpites
    if pc == jogador:
        print('\033[34mParabéns, você venceu\033[m')
    else:
        if jogador < pc:
            print('Mais...Tente mais uma vez')
        else:
            print('Menos...Tente mais uma vez')
print('Você precisou de {} palpites para vencer'.format(palpites))

