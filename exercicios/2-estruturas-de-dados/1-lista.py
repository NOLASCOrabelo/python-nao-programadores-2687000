lista=[]
numerica=[1, 2, 3, 4]
tiposeestruturadedados =['numerica', 'mista', 'extend', 'adicionais', 'append', 'remove', 'pop', 'slicen']
print(tiposeestruturadedados)
['numerica', 'mista', 'extend', 'adicionais', 'append', 'remove', 'pop', 'slicen']

tiposeestruturadedados[0:5]
['numerica', 'mista', 'extend', 'adicionais', 'append']

tiposeestruturadedados[0:-1:2]
['numerica', 'extend', 'append', 'pop']

tiposeestruturadedados.pop()
'slicen'

tiposeestruturadedados_adicionais=['slice']
tiposeestruturadedados.extend(tiposeestruturadedados_adicionais)
print(tiposeestruturadedados)
['numerica', 'mista', 'extend', 'adicionais', 'append', 'remove', 'pop', 'slice']

tiposeestruturadedados.remove('mista')
print(tiposeestruturadedados)
['numerica', 'extend', 'adicionais', 'append', 'remove', 'pop', 'slice']