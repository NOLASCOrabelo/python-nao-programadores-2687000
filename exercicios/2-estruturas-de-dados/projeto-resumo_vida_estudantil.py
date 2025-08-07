
cliente = { }

cliente['nome'] = input('Seu nome: ')
cliente['valor_de_renda'] = int(input('Valor a ser aplicado: '))
cliente['investimento'] = int(input('Tempo que deseja investir(em meses): '))







total_valor = cliente['valor_de_renda'] * cliente['investimento']


print(f"Segue os números {cliente['nome']}, com você aplicando {cliente['valor_de_renda']}, por {cliente['investimento']} mes(s), você terá {total_valor}")