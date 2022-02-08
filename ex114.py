# crie um código que teste se o código pudim está acessivel pelo computador usado
# para acessar um site no python usa-se a biblioteca urllib
# para o receber o site, use o request.urlopen('url') e para recerber o código basta usar o .read()

from urllib import request

try:
    n = request.urlopen("https://www.google.com")
except:
    print('o site google.com não está acessivel por essa máquina')
else:
    print('o site google.com está completamente acessivel por essa máquina')
