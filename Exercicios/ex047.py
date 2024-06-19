soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Informe o {}º número: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Você informou {} números \033[31mPARES\033[m e a soma é {}'.format(cont,soma))
