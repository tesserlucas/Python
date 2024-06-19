print('\033[31m-'*25)
print('Sequência de Fibonacci')
print('-\033[m'*25)
n = int(input('Quantos termos você quer mostrar ? '))
print('~'*35)
a = 0
b = 1
cont = 3
print('{} → {}'.format(a,b),end='')
while cont <= n:
        c = a + b
        print(' → {}'.format(c),end='')
        a = b
        b = c
        cont = cont  + 1
print(' → FIM')

