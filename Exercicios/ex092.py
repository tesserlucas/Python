# primeiro exercicio com funções
def area(l,c):
    a = l*c
    print(f'A área de um terreno {l}x{c} é de {a}m²')

#Programa principal
print('CONTROLE DE TERRENOS')
print('-'*20)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l,c) #área vai ser o valor de l e multiplicado pelo valor de c.
