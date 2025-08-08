numeros = list(range(101))
lista = [] # Here, we create new list because, i´ like that way 
print(numeros)  # print the original list


# Here we have one loop for percorring the all elements of list
for numero in numeros:
    if numero % 7 == 0 and numero % 4 == 0:
        lista.append('God')
    elif numero % 5 == 0:
        lista.append('In')
    elif numero % 9 == 0:
        lista.append('Live')
    else:
        lista.append(numero)
# I lie, we create the new list, for only whne to the number goes divisible, was goes add in the list a string

print(lista)  # Print the new list