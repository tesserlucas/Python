# Crie um código em Python que teste se um site está acessível pelo
# computador usado.

import urllib
import urllib.request

try:
    site=urllib.request.urlopen('https://ge.globo.com/') #Vou tentar abri a URL de um site
except urllib.error.URLError:
    print('O site do Globo Esporte não está acessível no momento')
else:
    print('Consegui abrir o site do Globo Esporte com sucesso!')
