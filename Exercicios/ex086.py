situacao = {}
lista = list()
a = 0
for c in range(0,1):
    situacao['nome'] = str(input('Nome do aluno: '))
    situacao['media'] = float(input(f'Média de {situacao["nome"]}: '))
    if situacao['media'] >=7:
        situacao['situação'] = 'Aprovado'
    elif 5 <= situacao['media'] < 7:
        situacao['situação'] = 'Recuperação'
    else:
        situacao['situação'] = 'Reprovado'
    lista.append(situacao.copy())
for s in lista:
    for k,v in s.items():
        print(f'O {k} é igual a {v}')
