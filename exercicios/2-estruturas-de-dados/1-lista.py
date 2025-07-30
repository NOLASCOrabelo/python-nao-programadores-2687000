numerica=[1, 2, 3, 4]

Mercuri =['Thiago', 20, 2005, ['adicionais', 'append', 'remove', 'pop', 'slicen'], True, ['python', 'sql','java'], False]

Mercuri[0:5]


elemento_indice_par=Mercuri[::2]
print(elemento_indice_par)

Mercuri.pop()
print(Mercuri)

Mercuri.append('Linux')
print(Mercuri)


Mercuri.remove('Linux')
print(Mercuri)
