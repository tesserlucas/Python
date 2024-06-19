tot = 0
cont = 0
menor = 0
barato = ''
totmil = 0
print('-'*25)
print('LOJA DO PEREIRÃO')
print('-'*25)
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$ '))
    cont = cont + 1
    tot = tot + valor
    if valor > 1000:
        totmil = totmil + 1
    if cont == 1 or valor < menor: #significa que só vai aconter se cont for igual a 1 ou se o valor for menor que menor preço
        menor = valor
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]
    if resp == 'N':
        break
print('\033[32m----------- COMPRAS FINALIZADAS ----------\033[m')
print(f'O valor total foi de R$ {tot:.2f}')
print(f'Tem {totmil} produtos que custam mais de R$ 1000')
print(f'O produto de menor valor é o/a {barato} que custa R$ {menor}')