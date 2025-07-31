# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:

# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome= input('Qual é seu nome?')
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias=input('Quantos dias você estuda por semana?')
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas=input('Qual a média de horas que realiza seus estudos?')
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso=input('Qual curso está cursando?')
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.

total_dias=int(total_dias)
total_horas=int(total_horas)




print(f'Olha só {nome}, você estuda {total_dias} dia(s), por semana em mais ou menos {total_horas} hora(s) por dia(s), e uma média de {total_dias*total_horas} horas semanal, para o curso {curso}')