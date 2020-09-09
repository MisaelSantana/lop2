class tratar_texto:
  def __init__(self, email, cpf, palindromo, url, html, telefone):
    self.email = email
    self.cpf = cpf
    self.palindromo = palindromo
    self.url = url
    self.html = html
    self.telefone = telefone

  def setEmail(self, email):
    self.email = email

  def setCpf(self, cpf):
    self.cpf = cpf

  def setPalindromo(self, palindromo):
    self.palindromo = palindromo

  def setUrl(self, url):
    self.url = url

  def setHtml(self, html):
    self.html = html

  def setTelefone(self, telefone):
    self.telefone = telefone


# VERIFICAÇÃO DE EMAIL

email = 'seila@bar.com.uk'
posicao_arroba = email.find('@')
posicao_ponto = email.find('.', posicao_arroba)

print('posicao @ : ' + str(posicao_arroba))
print('posicao . : ' + str(posicao_ponto))

if((posicao_arroba >= 0) and (posicao_ponto > posicao_arroba)):
  print(email + ' é um email válido')
else:
  print(email + ' é um email inválido')

posicao_uk = email.find('.uk', posicao_arroba)
if((posicao_arroba >= 0) and (posicao_uk > posicao_arroba)):
  print('Não recebemos emails de nação estrangeira')


# VERIFICAÇÃO DO CPF





# VERIFICAÇÃO PALINDROMO





# VERIFICAÇÃO URL

url = 'urlColocadaNessaPossicao'
vetorUrl1 = url.split('?')
print(vetorUrl1)
parametros = vetorUrl1[1].split('&')
print(parametros)
for x in parametros:
  parametros = x.split ('=')
  print(parametros[0] + ' : ' + parametros[1])


# VERIFICAÇÃO DA TAG IMG NA URL




# VALIDAÇÃO DO TELEFONE




