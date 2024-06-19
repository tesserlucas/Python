from math import factorial
n = int(input('Digite um número: '))
c = n # esse c é o contador
f = factorial(n)
print('Calculando fatorial de {}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ',end='') # comando feito para ter um x quando c é maior que 1 se não mostra um igual
    c = c - 1
print('{}'.format(f))