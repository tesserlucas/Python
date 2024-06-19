valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor dicionado...')
    else:
        print('Valor igual, não vou adicionar...')
    op =' '
    while op not in 'SN':
        op = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]
    if op == 'N':
        break
valores.sort()
print("-"*30)
print(f'Você digitou os valores: {valores}')
print("-"*30)
