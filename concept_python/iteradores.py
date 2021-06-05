from concept_python.generadores import my_gen


my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# print(type(my_iter))

# Extraer los elementos:

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# de forma sencilla esto es lo que hace un ciclo for por debajo, al encontrarse la excepción de StopIteration el ciclo para.
