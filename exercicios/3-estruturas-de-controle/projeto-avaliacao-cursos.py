Cliente = ['Thiago', '20 anos', 'cabelo preto', 'nariz grande', 'cílios']

rosto = 'nariz grande'
nome = 'Thiago'
idade = '20 anos'

Pessoa = {}

if rosto in Cliente:
  print(f'A característica {rosto} existe. Responda abaixo o que acha dela ') 
  Pessoa [rosto] = int(input('Qual a nota para essa carecterística? '))

if idade in Cliente:
  print(f'A característica {idade} existe. Responda abaixo o que acha dela ') 
  Pessoa [idade] = int(input('Qual a nota para essa carecterística? '))

if nome in Cliente:
  print(f'A característica {nome} existe. Responda abaixo o que acha dela ') 
  Pessoa [nome] = int(input('Qual a nota para essa carecterística? '))
else:
  print(f'Essa carecterística não existe X')
 
