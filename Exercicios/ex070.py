from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10))
menor = min(n)
maior = max(n)
print(f'Os valores sorteados foram: {n}')
print(f'O menor valor sorteado foi: {menor}')
print(f'O maior valor sorteado foi: {maior}')