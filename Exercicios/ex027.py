from random import randint
from time import sleep
pc = randint(0, 5) #Faz o pc pensar em um número de 0 a 5
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('PROCESSANDO...')
sleep(2) #comando usado para o tempo que ele vai ficar processando o print acima
print('-=-' * 10)
jogador = int(input('Em que número eu pensei ? ')) #Jogador tenta advinhar
if jogador == pc:
    print('Parabéns você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(pc,jogador))

