#Exemplo utilizando o return. 

def somar(a=0,b=0,c=0): # aqui esse c = 0 significa que se por acaso o C não receber valor nenhum ele vai valer zero.
    #isso seria um parâmetro opcional.
    soma = a + b + c
    return soma #comando para retornar o valor da soma.


r1 = somar(2,3,5) #preciso declarar r1 pois se não declarar ele não vai retornar nada.
r2 = somar(2,2) #preciso declarar r2 pois se não declarar ele não vai retornar nada.
r3 = somar(6) #preciso declarar r3 pois se não declarar ele não vai retornar nada.
print(f'Os resultados foram {r1}, {r2} e {r3}')