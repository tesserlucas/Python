n = 0
s = 0 
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break # Esse break é para que quando o número for igual a 999 ele sai e mostra a soma
    s = s + n # A soma só vai acontecer se o número não for 999
# print('A soma entre os números digitados é {}'.format(s))
# Outra maneira de usar o print com fstring
print(f'A soma vale {s}') # Esse f significa fstring 
