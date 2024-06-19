from random import randint


def sorteio(lista):
    print('-'*60)
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n) # vai sortear 5 números entre 1 e 10.
        print(f'{n} ', end='', flush=True)
    print('PRONTO!')

def pares(lista):
    soma = 0
    for valor in lista:
        if valor %2 ==0:
            soma = soma + valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
    print('-'*60)


#Programa principal
numeros = list()
sorteio(numeros)
pares(numeros)
