
estudante = { }


estudante['nome'] = input('Qual seu nome?')
estudante['ano_que_conheceu_o_linkedin'] = int(input('Quando conheceu o Linkedin?' ))
estudante['ano_atual'] = int(input('E o ano atual? '))
cursos = input('Quais cursos realizou?Todos separados por virgula e ordem cronologica:')
 
estudante['cursos'] = cursos.split(', ')






total_anos = estudante['ano_atual'] - estudante['ano_que_conheceu_o_linkedin']
total_cursos = len(estudante['cursos'])

print(f"Como vai {estudante['nome']}, o ano que conheceu o Linkedin foi {estudante['ano_que_conheceu_o_linkedin']}, Durante esses {total_anos} anos, você realizou {total_cursos} cursos, sendo o primeiro curso realizado {estudante['cursos'][0]}, e o último sendo {estudante['cursos'][-1]}")