valores = list()
maior = 0
menor = 0
for cont in range(0,5):
    valores.append(int(input('Digite um número: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c+1}...', end='')
print()
print(f'O menor valor digitado foi o {menor} nas posições ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c+1}...', end='')
print()
