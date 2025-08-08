
# criação de lista
Cliente = ['Thiago', '20 anos', 'cabelo preto', 'nariz grande', 'cílios']

#criação de variaveis para serem usadas junto com a lista
rosto = 'nariz grande'
nome = 'Thiago'
idade = '20 anos'

# Dicionario vazio, para ser inplementado durante o code
Pessoa = {}

# estrutura condicional para verificar se tal item está na lista e se estiver, deverá avaliar com uma nota
if rosto in Cliente:
  print(f'A característica {rosto} existe. Responda abaixo o que acha dela ') 
  Pessoa [rosto] = int(input('Qual a nota para essa carecterística? '))

if idade in Cliente:
  print(f'A característica {idade} existe. Responda abaixo o que acha dela ') 
  Pessoa [idade] = int(input('Qual a nota para essa carecterística? '))

if nome in Cliente:
  print(f'A característica {nome} existe. Responda abaixo o que acha dela ') 
  Pessoa [nome] = int(input('Qual a nota para essa carecterística? '))

# Caso não estiver, mensagem de "Erro"
else:
  print(f'Essa carecterística não existe X')

# Imprimir na tela o dicionário criado durante o code
print(Pessoa)

 
