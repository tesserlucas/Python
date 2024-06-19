from datetime import date
ano = int(input('Digite um ano qualquer: '))
if ano == 0:
    ano = date.today().year #Esse comando vai pegar o ano atual da máquina.
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano \033[31m {} \033[m não é bissexto'.format(ano))