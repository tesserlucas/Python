print('-'*30)
print('Programa nome e peso de pessoas'.upper())
print('-'*30)
nome = list()
peso = list()
mai = men = 0
while True:
    nome.append(str(input('Digite seu nome: ')))
    nome.append(float(input('Digite seu peso: ')))
    if len(peso) ==0:
        mai = men = nome[1]
    else:
        if nome[1] > mai:
            mai = nome[1]
        if nome[1] < men:
            men = nome[1]
    peso.append(nome[:])
    nome.clear()
    op = " "
    while op not in "SN":
        op = str(input('Quer continuar [S/N] ? ')).upper()
    if op == "N":
        break
print('-='*35)
print(f'Você cadastrou {len(peso)} pessoas no total')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in peso:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in peso:
    if p[1] == men:
        print(f'{p[0]} ', end='')
print()
print('-='*35)