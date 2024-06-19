print('-'*30)
print('<<< CADASTRO DE PESSOAS >>>')
print('-'*30)
pessoas = {}
lista = list()
media = 0
soma = 0
# neste código tem alguns dicionários dentro de uma lista
while True:
    pessoas.clear()
    pessoas['nome']=str(input('Nome: '))
    while True:
        pessoas['sexo']= str(input('Sexo [M/F]: ')).upper()
        if pessoas['sexo'] not in 'MF':
            print('ERRO! Tente novamente')
        else:
            break 
    pessoas['idade']= int(input('Idade: '))
    soma = soma + pessoas['idade'] #comando para calcular a média de idade
    lista.append(pessoas.copy())
    op = " "
    while op not in "SN":
        op = str(input('Quer continuar [S/N] ? ')).upper()
        if op not in 'SN':
            print('ERRO! Somente S ou N')
    if op == "N":
        break # da linha 4até a linha 27 é a leitura dos dados
print('-='*35) # da linha 28 até o final é o resultado dos dados
print(f'A) Ao total foram cadastradas {len(lista)} pessoas')
media = soma / len(lista) #comando para calcular a média de idade
print(f'B) A média de idade é de {media:.2f} anos ')
print('C) As mulheres cadastradas foram: | ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} | ', end='')
print()
print('D) Lista das pessoas acima da média')
for p in lista:
    if p['idade'] >= media:
        print('    ', end='')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('-='*35)
print('<<< FINALIZADO >>>')