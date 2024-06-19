from _datetime import date
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento: '))
    data = date.today().year
    total = data - ano
    if total >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Ao todo tivemos {} pessoas de maior idade e \n{} pessoas de menor idade'.format(totmaior,totmenor))