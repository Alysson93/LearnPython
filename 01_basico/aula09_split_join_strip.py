frase = ' Estou aprendendo programação '
lista = []

separa = frase.split(' ')
print(separa)

junta = ' '.join(separa)
print(junta)

#strip remove espaços vazios do início e do fim
print(frase)
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())