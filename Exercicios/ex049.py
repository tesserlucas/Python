n = int(input('Digite um valor: '))
tot =0
for c in range(1, n + 1):
    if n % c == 0:
        print(c, end=' ')
        tot = tot + 1
    else:
        print(c,end=' ')
print('\nO número {} foi divisivel {} vezes'.format(n,tot))
if tot == 2:
    print('É por isso que ele é primo')
else:
    print('Por isso ele não é primo')