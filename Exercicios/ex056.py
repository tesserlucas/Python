from time import sleep
n1 = float(input('1º valor: '))
n2 = float(input('2º valor: '))
op = 0
while op != 5:
    print('='*10)
    print('OPÇÕES')
    print('=' * 10)
    print('\033[1;32m[1]- Somar\n[2]- Multiplicar\n[3]- Maior\n[4]- Novo valor\n[5]- Sair\033[m')
    op = int(input('Escolha uma das opções: '))
    print('=-' * 25)
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {} '.format(n1,n2,soma))
    elif op == 2:
        multi = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1,n2,multi))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('0 maior é {}'.format(maior))
    elif op == 4:
        print('Informe os valores novamente')
        n1 = float(input('1º valor: '))
        n2 = float(input('2º valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Comando inválido')
    sleep(1)
    print('=-'*25)
print('Fim do programa! Volte Sempre!')