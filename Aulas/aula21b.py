#Exemplo 1:

print('\033[1;31mEXEMPLO 1\033[m')
def contador(i,f,p):
#essas 3 aspas abaixo com o texto seria a minha docstrings, que no caso é o manual da minha função contador. 
    """
    -> Faz a contagem e mostra na tela. 
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <=f:
        print(f'{c}', end='..')  
        c = c + p
    print('FIM!')   


#Programa Principal
#temos o inicio que é o 2, o fim que é o 10 e o passo que é o 2.
#No caso o programa inicia em 2 vai até 10 pulando de 2 em 2.
contador(2,10,2)
help(contador)

print('-='*25)

#Exemplo 2.

print('\033[1;31mEXEMPLO 2\033[m')
def somar(a=0,b=0,c=0): # aqui esse c = 0 significa que se por acaso o C não receber valor nenhum ele vai valer zero.
    #isso seria um parâmetro opcional.
    """
    -> Faz a soma de 3 valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    soma = a + b + c
    print(f'A soma vale {soma}')


somar(2,3,5)
somar(4,8) #aqui como declarei o c = 0, ele vai considerar o valor 0. Se tiver valor no C ele vai somar
somar()
help(somar) #função para ver a documentação da função.