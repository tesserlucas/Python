from datetime import date
print('-------------------------')
print('Alistamento Militar')
print('-------------------------')
nome = input('Digite o nome da pessoa: ')
ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
tempo = idade - 18
print('Sr. {} você já está com {} anos'.format(nome,idade))
if idade > 18:
    print('Sr. {} você devia ter se alistado a {} anos'.format(nome,tempo))
    print('Sr {} seu alistamento foi em {}'.format(nome, ano+18))
elif idade == 18:
    print('Sr. {} você deve ser alistar'.format(nome))
else:
    print('Sr. {} falta ainda {} anos para seu alistamento'.format(nome,18 - idade))
    print('Seu alistamento será em {}'.format(ano+18))
