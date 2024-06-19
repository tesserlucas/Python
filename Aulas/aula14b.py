n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n !=0: #todo esse teste abaxio só vai funcionar se o n for diferente de 0
        if n %2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} pares e {} ímpares'.format(par,impar))