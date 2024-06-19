cont = 0
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehomem = ''
for c in range(1,5):
    print('-------- {}º pessoa --------'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F] ? '))
    somaidade = somaidade + idade
    if sexo == 'F' and idade < 20:
        cont = cont + 1
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomehomem = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomem = nome
mediaidade = somaidade/4
print('A soma de idade do grupo é {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomehomem))
print('Tem {} mulheres com menos de 20 anos'.format(cont))

