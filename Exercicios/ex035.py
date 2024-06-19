n = int(input('Digite um valor inteiro: '))
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
op = int(input('Sua opção: '))
if op == 1:
    print('O número {} em binário é {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('O número {} em OCTAL é {}'.format(n,oct(n)[2:]))
elif op == 3:
    print('O número {} em HEXADECIMAL é {} '.format(n,hex(n)[2:]))
else:
    print('Opção inválida')
