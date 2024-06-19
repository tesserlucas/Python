n = 0
cont = 0
soma = 0
n = int(input('Digite um valor [999 para sair]: '))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('Digite um valor [999 para sair]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont,soma))