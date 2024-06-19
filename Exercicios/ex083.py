print('-'*15)
print('ANALISANDO A MATRIZ 3X3')
print('-'*15)
matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
pares = 0
maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        soma = soma + matriz[l][2] #fazer um for da linha pois a coluna já é fixa
    if c == 0:
        maior = matriz[1][c]
    elif matriz [1][c] > maior:
        maior = matriz[1][c]
print("-="*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')#esse :^5 é para centralizar com 5 espaços
        if matriz[l][c] % 2 ==0:
            pares = pares + matriz[l][c]
    print() #esse print é para quebrar linha e imprimir de forma correta 
#sem esse print iria imprimir os números em uma única linha e não em 3x3
print("-="*30)
print(f'A soma da terceira coluna é: {soma}')
print(f'A soma é: {pares}')
print(f'O maior valor da segunda linha é: {maior}')
print("-="*30)