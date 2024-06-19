lista = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    op = " "
    while op not in 'SN':
        op = str(input('Quer continuar [S/N] ? ')).upper().strip()
    if op == 'N':
        break
lista.sort()
pares.sort()
impares.sort()
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista completa de ímpares é: {impares}')