sexo = str(input('SEXO [M/F] ')).upper().strip()[0]
while sexo not in 'MF': # enquanto o sexo nao for M ou F ele retorna isso.
    sexo = str(input('Dados inválidos. Por favor informe o sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))