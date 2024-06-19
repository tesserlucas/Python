print('-'*25)
print('Validando expressões matemáticas')
print('-'*25)
exp = str(input('Digite uma expressão: '))
pilha = list()
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')