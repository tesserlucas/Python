cont = 0
homem = 0
totM20 = 0
print('-'*20)
print('CADASTRO DE PESSOAS')
print('-'*20)
while True:
    idade = int(input('Idade da pessoa: '))
    sexo =' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] ? ')).upper().strip()[0]
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    op =' '
    while op not in 'SN':
        op = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]
    if op == 'N':
        break
print(f'Quantidade de homens cadastrados: {homem}')
print(f'Quantidade de pessoas maiores de 18 anos: {cont }')
print(f'E temos {totM20} mulheres com menos de 20 anos')