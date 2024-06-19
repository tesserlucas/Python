lista = list()
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]
    if op == 'N':
        break
lista.sort(reverse=True)
print("-="*30)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
        print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
print("-="*30)

