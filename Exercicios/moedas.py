def metade(n=0, format=False):
    res = n / 2
    return res if format is False else moeda(res) # se format for falso, retorna res, senão, retorna res formatado

def dobro(n=0, format=False):
    res = n * 2
    return res if format is False else moeda(res)

def aumentar(n=0,taxa=0, format=False):
    res = n + (n*taxa/100)
    return res if format is False else moeda(res)


def dimunuir(n=0,taxa=0,format=False):
    res = n - (n*taxa/100)
    return res if format is False else moeda(res)

def moeda(n=0,moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')

def resumo(n=0,taxaa=10,taxar=15):
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*35)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço:  \t{dobro(n,True)}')
    print(f'Metade do preço: \t{metade(n,True)}') 
    print(f'Com {taxaa}% de aumentar: \t{aumentar(n,taxaa,True)}') #esse \t é para ficar formatado
    print(f'Com {taxar}% de redeução: \t{dimunuir(n,taxar, True)} ') # esse True é para formatar
    print('-'*35)