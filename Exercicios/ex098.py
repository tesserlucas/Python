#Exercicio: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
#o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico 
#(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número. 
    :param num: O número a ser calculado. 
    :param show: (opcional) Mostrar ou não a conta. 
    :return: O valor do Fatorial de um número num. 
    """
    f = 1
    for c in range(num,0,-1):
        if show:
            print(c, end='')
            if c > 1: #Se o contador for maior que 1 ele vai mostrar o x
                print(' x ', end='')
            else: #Se o contador for igual a 1 ele vai mostrar o =
                print(' = ', end='')
        f = f*c
    return f #retorna o valor da função para o programa principal 

print('-='*20)
print('CONTA FATORIAL')
print(fatorial(5, show=True)) #Se colocar o show=True ele mostra o processo de calculo do fatorial
print('-='*20)
print('       Manual da função fatorial'.upper())
print('-='*20)
help(fatorial)
