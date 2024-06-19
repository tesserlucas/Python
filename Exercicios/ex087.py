from random import randint
from time import sleep
from operator import itemgetter #usado para mostrar a ordem da parte1 no caso ali o jogador1,jogador2,...
jogador = {'jogador1':randint(1,6),
           'jogador2':randint(1,6),
           'jogador3':randint(1,6),
           'jogador4':randint(1,6)}
ranking = list()
print('-='*20)
print('          VALORES SORTEADOS   ')
print('-='*20)
for k,v in jogador.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True) #comando essencial do exercicio
print('-='*20)
print('\033[31m== RANKING DOS JOGADORES ==\033[m')
for i,v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}. ')
    sleep(1)