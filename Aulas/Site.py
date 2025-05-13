#  antigo site pudim

# from requests import get

# url = 'http://www.pudim.com.br/'

# try:
#     resposta = get(url)
#     print('Site Pudim acessado com sucesso!')
# except:
#     print('Site Pudim não pode ser acessado no momento.')

def sitefunciona(link):
    import urllib # importa a biblioteca
    import urllib.error # atributos da biblioteca
    import urllib.request

    try:
        site = urllib.request.urlopen(link) # usando o request, tenta abrir o link no navegador
    except urllib.error.URLError: # caso não consiga, com o atributo error, podemos verificar se foi um URLError (não conseguiu abrir o url)
        print('Site não pode ser acessado no momento.')
    else:
        print('Site acessado com sucesso!')
        print(site.read()) # mostra o codigo do site inteiro


sitefunciona('https://www.youtube.com/watch?v=6Y5NSoTCDVM') # modo de dizer - jão



