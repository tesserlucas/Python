print('-'*30)
print('BOLETIM COM LISTAS COMPOSTAS')
print('-'*30)
lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2)/2
    lista.append([nome,[nota1, nota2], media])
    op = " "
    while op not in "SN":
        op = str(input('Quer continuar [S/N] ? ')).upper()
    if op == "N":
        break
print('-='*20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*20)
for i,a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-'*40)
while True:
    a = int(input('Você quer ver a média de qual aluno ? (999 para finalizar)'))
    if a == 999:
        print('-'*40)
        print('FINALIZANDO...')
        print('-'*40)
        break
    if a <= len(lista)+1:
        print('-'*40)
        print(f'Notas de {lista[a][0]} são {lista[a][1]}')
        print('-'*40)
print('<<<<< VOLTE SEMPRE >>>>>')
