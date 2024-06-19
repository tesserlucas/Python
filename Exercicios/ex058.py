print('='*35)
print('10 PRIMEIROS TERMOS DE UMA P.A')
print('='*35)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
termo = t
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo),end='')
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
print('FIM')