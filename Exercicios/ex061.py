r = 'S'
media = 0
maior = 0
menor = 0
cont = 0
soma = 0
while r == 'S':
    n = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + n
    media = soma/cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    r = input('Você quer continuar [S/N] ? ').upper().strip()[0]#este 0 significa considerar a primeira letra só
print('Você digitou {} números e a média entre eles foi de {:.2f}'.format(cont,media))
print('O menor valor foi o {} e o maior valor foi o {}'.format(menor,maior)) 

