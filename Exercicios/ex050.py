n = (str(input('Digite algo: '))).strip().upper()
palavra = n.split()
junto = ' '.join(palavra)
inverso = ''
for c in range (len(junto)-1,-1,-1):
    inverso = inverso + junto[c]
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
print('0 inverso de {} é {}'.format(n,n[::-1]))