nome= input('Qual é seu nome?')

total_dias=input('Quantos dias você estuda por semana?')

total_horas=input('Qual a média de horas que realiza seus estudos?')

curso=input('Qual curso está fazendo?')

total_dias=int(total_dias)
total_horas=int(total_horas)




print(f'Olha só {nome}, você estuda {total_dias} dia(s), por semana em mais ou menos {total_horas} hora(s) por dia(s), e uma média de {total_dias*total_horas} horas semanal, para o curso {curso}')