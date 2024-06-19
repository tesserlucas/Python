valores = list()
for cont in range(0,5):
    n = (int(input('Digite um valor: ')))
    if cont == 0:
        valores.append(n)
    elif n > valores[len(valores)-1]:
        valores.append(n)
    else:
        pos = 0 
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break 
            pos = pos + 1
print(f'A lista em ordem dos valores digitados é: {valores}')
