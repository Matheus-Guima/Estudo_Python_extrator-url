################################# Manipulação de String ################################################################
#Url = https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100

# site = https://bytebank.com/cambio?
# cambio = pagina
# & = separador
# variaveis = moedaOrigem=real; moedaDestino=dolar; dolar&quantidade=100


################################### MÉTO DE FATIAMENTO #################################################################

#Fatiamento passa duas posições, pposição de inínio e de fim, da onde vc quer extrair da string
#Onde o primeiro argumento (caracter) é inclusivo e o segundo é exclusivo
#Ex: texto = 'abcd' --> texto[0:1] --> vai retornar --> 'a'
#Mas se quiser 'a' e 'b' tem que pesquisar ---> texto[0:2] ---> retorna --> 'ab'
#Fatiamento não altera a URL original, só faz uma cópia
#string no python são imutáveis
#Artigo sobre mutabilidade de string do pyhton = https://blog.saldanha.dev/imutabilidade-de-strings-no-python

url = "https://bytebank.com/cambio?moedaOrigem=real"
print("################## AULA 1 ###############")
print(url)

url_base = url[0:27] #Faz o método de fatiamento para pegar base da url
print(url_base)

url_parametros = url[28:44] #Faz o método de fatiamento para pegar parametros da url
print(url_parametros)

################################### MÉTODO FIND ########################################################################
#Procura a letra dentro da string
#Método Find tbm pode ser usado para procurar algo a partir de algum indice
#Ex: url.find("moeda", 30) a partir do indice 30, procura indice de "m" de moeda

indice_interrogacao = url.find('?')

url_base1 = url[:indice_interrogacao]    #Posso omitir o valor inicial, ele vai pensar que estou falando do inicio
url_parametros2 = url[indice_interrogacao+1:]   #Posso omitir o valor final, se eu quiser o ultimo valor da string

print("################## AULA 2 ###############")
print(url_base1, url_parametros2)

################################### AULA 3 #############################################################################
url2 = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"

indice_interrogacao_url2 = url2.find('?')
url_parametros3 = url2[indice_interrogacao_url2:]

parametro_de_busca ='moedaOrigem'
indice_parametro2 = url2.find(parametro_de_busca)
tamanho_parametro2 = len(parametro_de_busca)
indice_valor_real= indice_parametro2 + tamanho_parametro2 + 1

print("################## AULA 3 ###############")
print(indice_interrogacao_url2, "- INDICE INTERROGAÇÃO")
print(indice_parametro2, '- INDICE PARAMETRO 2 QUE É "M" de MOEDA DE BUSCA')
print(url2[indice_parametro2:])
print(url2[indice_valor_real:])

print("##### Simplificando #####")
#url2 = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
real = url2.find('real')
tamanha_real = len('real')
indice_valor = real + tamanha_real  #Para achar o valor "Real" na URL indice_do_parametro + tamanh0_d0_parametro
valor_real_sem_end = url2[real:]
valor_real = url2[real:indice_valor]
# print(valor_real)


indice_e_comercial = url2.find('&', indice_valor) #Se não achar retorna -1

if(indice_e_comercial == -1):
    print(valor_real_sem_end)
else:
    print(valor_real)














