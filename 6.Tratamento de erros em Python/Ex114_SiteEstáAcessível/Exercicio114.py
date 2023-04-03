"""Crie um código em Python que teste se o site pudim está acessível pelo computador usado. """

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site solicitado não está acessível no momento.')
else:
    print('O site está acessível')

# O site buscado em html, porém vem desorganizada

# print(site.read())

