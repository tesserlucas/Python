n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
media = (n1+n2+n3)/3
if media > 7.0:
    print('Aluno aprovado com média {:.2f}'.format(media))
elif media >=5 and media < 7:
    print('Aluno em recuperação com média {:.2f}'.format(media))
else:
    print('Aluno reprovado com média {:.2f}'.format(media))
