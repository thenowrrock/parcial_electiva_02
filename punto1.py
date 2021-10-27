
#Autores Juan David Jimenez 
'''
•Escriba un programa que tenga como entrada los
números de la serie de fibonacci. El programa
debe calcular el acumulado de los números para
un rango dado por el usuario así: Si el número a
computar es primo lo debe sumar al valor
acumulado y si no es primo lo debe elevar al
cuadrado y sumarlo al acumulado.

•Utilice funciones como map, filter y reduce.
•Valor del punto 1 = 1.0'''

from functools import reduce


#funcion que me recolecta los valores solicitados para el rango desde donde se quiere realizar la serie de fibonacci
def number():
    while True:
        user_input = input('Ingrese un numero mientras que no sea negativo  rango incial: ')
        user_input_2 =  input('Ingrese el rango final:')
        if user_input.isnumeric() and user_input_2.isnumeric(): #Si los 2 se cumplen , retorna los elementos que tienen .isnumeric() comprueba que sea un numero
            return int (user_input), int (user_input_2)        
        else:
            print("Error , continuar")
            continue
            
#Genera serie de fibonacci
generar_serie_fibo = lambda x: reduce(lambda n, _: n + [n[-1] + n[-2]], range(x - 2) , [0, 1])


#funcion que determina si un numero es primo 
def yes_primo(x):
    if x <=  1: #evaluamos el parametro de entrada si x <=  1 no es primmo  y retorna false
        return False
    for i in range(2, x- 1): #para todo numero primo siempre que el modulo de x % i sea  igual a 0  , se determina que es un numero primo retorna verdadero hasta antes de llegar al ultimo por analizar en la lista cuando se llega al ultimo retorna false para terminar el ciclo
        if x % i == 0: 
            return False
    return True     

#Defino los rangos , min y max 
min,max =  number()  #usamos nuestra funcion anteriormente creada number() que determina las entradas por consola que el usu digita
#fibo_list =  fibonacci(max) #lista que contiene la serie con el rango dado  y la fibonacci(max) que es la serie recibiendo el rango max hasta donde se va evaluar la serie.
fibo_list = generar_serie_fibo(max)


#imprimimos nuestra serie generada
print("Serie fibonacci: " , fibo_list)
#elementos de la serie
print("Cantidad elementos serie: " , len(fibo_list))    
        

#Creamos variables con la finalidad de filtrar nuestras listas de numeros
primo = list(filter(yes_primo, fibo_list)) #filtramos la lista de la serie de fibonacci  y determinamos si contiene numeros primos , si tiene primos los numeros quedaran almacenados en la lista primo
#filtro = set(fibo_list) - set(primo) #determinamos los elementos que esan en una lista y no en la otra, filtramos los numeros primo de la serie, que nos quedaria que serian los numeros que no son primos de nuestra serie y quedan guardados en la lista no_primo

#Filtramos los elemntos de una lista de la otra que no son primos 
lis1 = set(fibo_list)
lis2 = set(primo)
diferentes = lis1.difference(lis2)

#Numero que no son primos 
no_primo = list(map(lambda n: n**2 ,diferentes)) #aplicamos a la lista no primo la operacion de elevarlos al cuadrado

#Impresion de nuestros elementos filtrados
print("no primo :" , diferentes)
print("Numeros primos filtrados:",primo)
print("no primo al cuadrado :",  no_primo)

#Calcular  la suma de nuestros elementos de la listas 
primos_sum =  sum(primo)  #+ 1 #le sumo  + 1 , ya que cuando determinamamos los elementos que estan en una lista y no en la otra para tener los que no son primos , la funcion set() me quita el 2 elemento de mi lista y esto altera el resultado del acomulado esto pasa para cualquier rango.
no_primo_sum =  sum(no_primo) #sumamos el acomulado de la lista de no primo 

#Imprimimos sus totales 
print("suma primos_sum: ",primos_sum)
print("suma no_primo_sum: ",no_primo_sum)

#Calculamos el acomulado de toda la serie de fibonacci
suma_acomulado = primos_sum + no_primo_sum #sumamos las listas de los primos y no _ primos que serian el acomulado total

#Imprimimos nuestro acomulado
print("suma acomulado: ",suma_acomulado)





