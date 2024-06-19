from datetime import datetime
print('-='*15)
print('<<< CADASTRO DE TRABALHADOR >>>')
print('-='*15)
d = {}  
d['Nome']=str(input('Nome: '))
ano = int(input('Ano de Nascimento: ')) #a variavel ano não esta dentro do dicionário
d['Idade']= datetime.now().year - ano
d['Carteira de Trabalho']=int(input('Carteira de Trabalho (0 não tem): '))
if d['Carteira de Trabalho'] !=0:
    d['Contratação']=int(input('Ano de Contratação: '))
    d['Salário']=float(input('Salário R$: '))
    d['Aposentadoria'] = d['Contratação'] + 35 - ano
else:
    print()
print('-='*25)
for k,v in d.items():
    print(f'  - {k} tem valor {v}')
print('-='*25)