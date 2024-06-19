#Exercicio 1: Calcular o fatorial de um número utilizando o def
#e retornar ele para o meu programa principal para mostrar esse valor na tela.

print('\033[1;31mEXERCICIO 1\033[m')
def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f = f*c
    return f #retorna o valor da função para o programa principal

n = int(input('Digite um número: '))
print('-='*20)
print(f'O fatorial de {n} é igual a {fatorial(n)}') #vai imprimir o valor do fatorial de n

#Outra forma de fazer o mesmo exercicio:

f1 = fatorial(5) #vai pegar o valor de n e vai fazer o fatorial de 5 e vai retornar para o programa principal.
f2 = fatorial(4) #vai pegar o valor de n e vai fazer o fatorial de 4 e vai retornar para o programa principal.
f3 = fatorial() #vai pegar o valor de n e vai fazer o fatorial de 1 e vai retornar para o programa principal.
print('-='*20)
print(f'Os resultados são {f1}; {f2}; {f3}') #vai imprimir o valor de f1, f2 e f3.
print('-='*20)




#Exericio 2: fazer um programa com o def para ver se um número é par, se ele for par retornar true caso contrário
# retornar false.

print('\033[1;31mEXERCICIO 2\033[m')
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(par(num)) 

#Outra forma de fazer o mesmo exercicio:

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')