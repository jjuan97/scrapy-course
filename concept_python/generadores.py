# Un generador es una funcion que puede hacer un return y guardar el estado de la función.

def my_gen():
    a = 1
    yield a

    a = 2
    yield a

    a = 3
    yield a

my_first_gen = my_gen()
print(next(my_first_gen))
print(next(my_first_gen))
print(next(my_first_gen))
#print(next(my_first_gen))

print("\nSecond example:\n")

# generador que trae los 100 primeros numeros pares:

def my_gen_par_number():
    for number in range(0,200,2):
        yield number

par_number = my_gen_par_number()

while True:
    try:
        print(next(par_number))
    except:
        print("End iterationt")
        break