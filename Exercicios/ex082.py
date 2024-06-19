print('-'*15)
print('MATRIZ 3X3')
print('-'*15)
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print("-="*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')#esse :^5 é para centralizar com 5 espaços
    print() #esse print é para quebrar linha e imprimir de forma correta 
#sem esse print iria imprimir os números em uma única linha e não em 3x3