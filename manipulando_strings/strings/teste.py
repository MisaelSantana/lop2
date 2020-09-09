
teste = '123@2q'
print(type(teste))

# tamanho de uma string
print(len(teste))

# trocar caracteres
troca = teste.replace('2', 'abacate')
print('original: ' + teste)
print('replace: ' + troca)
# contar caracteres específicos
print('qtde letra a na string teste ' + str(teste.count('a')))
print('qtde letra a na string troca ' + str(troca.count('a')))

posicao = teste.find('123')  # encontra a posição de um caractere (1ª posição)
print(posicao)

if(posicao > 0):
    print(teste[posicao])
else:
    print('caractere não encontrado')

# verificar se o email é valido find(string_busca, inicio, fim)
email = 'foo@bar.com.uk'

posicao_arroba = email.find('@')
posicao_ponto = email.find('.', posicao_arroba)

print('posição @ : ' + str(posicao_arroba))
print('posição . : ' + str(posicao_ponto))
if((posicao_arroba >= 0) and (posicao_ponto > posicao_arroba)):
    print(email + ' é um email válido')
else:
    print(email + ' é um email inválido')

posicao_uk = email.find('.uk', posicao_arroba)

if((posicao_arroba >= 0) and (posicao_uk > posicao_arroba)):
    print('não aceitamos email do Reino Unido')

frase = 'O papa é pop - barão vermelho'
vetor1 = frase.split('-')
print(vetor1)

vetor2 = frase.split(' ')
print(vetor2)

meetUrl = 'https://meet.google.com/maq-bwyr-jjg?authuser=0&cor=blue&background=yellow&year=12'
vetorUrl = meetUrl.split('?')
print(vetorUrl)
parametros = vetorUrl[1].split('&')
print(parametros)
for x in parametros:
    parametro = x.split('=')
    print(parametro[0] + ' : ' + parametro[1])

# converter array em string
vetOriginal = ['authuser=0', 'cor=blue', 'background=yellow', 'year=12']
url = '&'

novaUrl = url.join(vetOriginal)
print('http://some.domain.com?' + novaUrl)

# converter para maiúsculo
nome = 'Pedro alvares de Cabral e SOUSA'
print(nome)
nome_convertido = nome.upper()
print(nome_convertido)

# converter para minúsculo
nome_convertido = nome.lower()
print(nome_convertido)

# converter apenas a primeira letra para maiusculo
nome_convertido = nome.lower().capitalize()
print(nome_convertido)

# converter apenas a primeira letra de cada palavra
nome_convertido = nome.title()
print(nome_convertido)

# trocar os case
nome_convertido = nome.swapcase()
print(nome_convertido)

# desafio deixar cada frase do texto iniciada em maiúscula
# (swapcase, title, capitalize, lower, upper, join, split, find, count, len, replace)
texto = 'o rei roeu as roupas do rato. Mas rato comeu o queijo do rei.'
vet_texto = texto.split('. ')
tamanho = len(vet_texto)
print(tamanho)
contador = 0
while(contador < len(vet_texto)):
    vet_texto[contador] = vet_texto[contador].capitalize()
    contador += 1

texto_convertido = '. '.join(vet_texto)
print(texto_convertido)


# checar se a string está em maiúsculo
texto = 'foo'.upper()
print(texto.isupper())

if(texto.isupper()):
    print('texto em maiúsculo')


if(texto.islower()):
    print('texto em minúsculo')


# checar se a string está em minúsculo
texto = 'foo'.lower()
print(texto.islower())

if(texto.isupper()):
    print('texto em maiúsculo')


if(texto.islower()):
    print('texto em minúsculo')

texto = 'a coroa do rei'.title()
if(texto.istitle()):
    print('isso é loucura')

# verifica se é alfa numérico
texto = '123ssse'

if(texto.isalnum()):
    print('é alfa-numérico')
else:
    print('parece ter algum caractere estranho')

# verifica se contem apenas letras

texto = 'asdfgh'

if(texto.isalpha()):
    print('possui apenas letras')
else:
    print('parece ter algum caractere estranho')

# verificar se possui apenas números
texto = '123456'

if(texto.isdigit()):
    print('possui apenas numeros')
else:
    print('parece ter algum caractere estranho')

# verificar se possui apenas números
texto = ''

if(texto.isspace()):
    print('possui apenas apenas espaço em branco')
else:
    print('parece ter algum caractere estranho')

# verificou se a string está vazia
if(len(texto) == 0):
    print('string vazia')
else:
    print('tem algo dentro dessa joça')
    print('tamanho da string ' + str(len(texto)))

# adicionar espaços em branco
texto = 'uma string'

nova_string = texto.ljust(30) + '!'  # à direito
print(nova_string)

nova_string = texto.rjust(30) + '!'  # à esquerda
print(nova_string)

nova_string = texto.center(30) + '!'  # à esquerda
print(nova_string)

# remover espaços em branco
string = '       uma     nova     string  123       '
string_padronizada = string.strip()

print(string)
print(string_padronizada + '!@#')

string_padronizada = string.rstrip()
print(string_padronizada + '!@#')

string_padronizada = string.lstrip()
print(string_padronizada + '!@#')


# + concatenar

teste = 'maria' + '    ' + 'foi à feira'
print(teste)

# * repete a string
teste = 'ha'*5
print(teste)
teste = 'k'*90
print(teste)


# Criar uma classe chamada TratarTexto
# criar métodos para:
# verificar se um email é .br e é um email válidos
# verificar se uma string é um cpf
# verificar se uma string é um palindromo
# verificar se uma string é uma url
# verificar se uma string posui a tag img do html
# verificar se a sting é um número de telefone celular - pode desconsiderar o dd
