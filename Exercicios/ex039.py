from datetime import date
print('----------------------------------')
print('Confederação nacional de natação')
print('----------------------------------')
nome = input('Nome do atleta: ')
ano = int(input('Ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('O atleta {} tem {} anos'.format(nome, idade))
    print('Atleta mirim')
elif idade >= 10 and idade <= 14:
    print('O atleta {} tem {} anos'.format(nome, idade))
    print('Atleta infantil')
elif idade >= 15 and idade <= 19:
    print('O atleta {} tem {} anos'.format(nome,idade))
    print('Atleta júnior')
elif idade >= 20 and idade <=25:
    print('O atleta {} tem {} anos'.format(nome,idade))
    print('Atleta sênior')
else:
    print('O atleta {} tem {} anos'.format(nome,idade))
    print('Atleta master')


