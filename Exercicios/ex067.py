print('-'*20)
print('CAIXA ELETRÔNICO')
print('-'*20)
saque = int(input('Qual valor deseja sacar: R$ '))
total = saque
ced = 100
totced = 0
while True:
    if total >= ced:
        total = total - ced 
        totced = totced + 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        totced = 0
        if total == 0:
            break
print('-'*25)
print('Volte Sempre ao Banco DEV')
print('-'*25)