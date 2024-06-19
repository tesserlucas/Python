lista = ('Palmeiras','Grêmio','Atlético-MG','Flamengo','Botafogo','Bragantino','Fluminense',
         'Athletico-PR','Internacional','Fortaleza','São Paulo','Cuiabá','Corinthians','Cruzeiro',
         'Vasco da Gama','Bahia','Santos','Goiás','Coritiba','América-MG')
print('-='*15)
print(f'Lista Brasileirão 2023 {lista}')
print('-='*15)
print(f'Os 5 primeiros colocados são: {lista[:5]}')
print('-='*15)
print(f'Os 4 últimos colocados são: {lista[16:20]}')
print('-='*15)
print(f'Os times em ordem alfabética: {sorted(lista)}')
print('-='*15)
print(f'O time do Internacional está na {lista.index("Internacional")+1}º posição')
print('-='*15)