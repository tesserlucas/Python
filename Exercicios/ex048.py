print('='*35)
print('10 PRIMEIROS TERMOS DE UMA P.A')
print('='*35)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = t + (10 - 1) * r
for c in range(t,decimo + r ,r):
    print(c)