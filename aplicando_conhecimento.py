url = "https://www.banco.com.br/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

indice_interrogacao = url.find('?')

url_pura = url[:indice_interrogacao]
texto_url = url[indice_interrogacao+1:]

print(url_pura)
print(texto_url)
print('-----------------------')

palavra = 'real'
tamanho_palavra = len(palavra)
indice_palavra = url.find(palavra)
palavra_completa = indice_palavra + tamanho_palavra
# print(url[indice_palavra:palavra_completa])

indice_e_comercial = url.find('&', palavra_completa)
# print(indice_e_comercial, 'indice &', url[67])

indice_igual = url.find('=', palavra_completa)
# print(indice_igual, 'indice =', url[78])

palavra_c_tratamento = url[indice_palavra:palavra_completa]
palavra_sem_tratamento = url[indice_palavra:]

if(indice_e_comercial and indice_igual >= 0):
    print(palavra_c_tratamento.upper(), 'Precisou de tratamento')
else:
    print(palavra_sem_tratamento.upper(), '- Não precisou de tratamento')






# indice_interrogacao = url.find('?')
# url_base = url[:indice_interrogacao]
# url_parametros = url[indice_interrogacao+1:]
# print(url_parametros)
#
# parametros_busca ='quantidade'
# indice_parametro = url_parametros.find(parametros_busca)
# print(indice_parametro)