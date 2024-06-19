#Exercicio:  Crie um programa que tenha uma função chamada voto() que vai receber como 
#parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se 
#uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano_nascimento): 
    from datetime import date  #deixar esse comando dentro do def economiza memoria, pois ele só vai ser executado uma vez
    atual = date.today().year 
    idade = atual - ano_nascimento 

    if idade < 16: 
        return f'Com {idade} anos: NÃO VOTA.' 
    elif idade > 16 and idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade >=18 and idade <= 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


#Programa principal
ano = int(input('Em que ano você nasceu ? '))
print(voto(ano))