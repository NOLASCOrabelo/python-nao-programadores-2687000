# Aqui fazemos um dicionário vazio
cliente = { }

# Aqui criamos e colocamos values dentro do dicionário
cliente['nome'] = input('Seu nome: ')
cliente['valor_de_renda'] = int(input('Valor a ser aplicado: '))
cliente['investimento'] = int(input('Tempo que deseja investir(em meses): '))

# Aqui criamos uma variavel para juntar o value dentro do dicionário e multiplicar com outro value do mesmo dicionário
total_valor = cliente['valor_de_renda'] * cliente['investimento']

# Por fim imprimimos o dicionário junto com os values atribuidos a ele e o resultado final.
print(f"Segue os números {cliente['nome']}, com você aplicando {cliente['valor_de_renda']}, por {cliente['investimento']} mes(s), você terá {total_valor}")