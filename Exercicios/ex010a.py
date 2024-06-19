n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A média final entre {} e {} do aluno é {:.2f}'.format(n1, n2, media))
if media >=6:
    print('Aluno Aprovado')
else:
    print('Aluno Reprovado')