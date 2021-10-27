#Autores Juan David Jimenez
'''
•Escriba un programa en python que utilizando
expresiones lambda devuelva los números de la
siguiente serie:

            (2n)!
            (n + 1)!n!

•Para generar los n números a calcular en la serie,
utilice una función generadora de números
enteros mayores a 0.


•Punto No. 2
Valor del punto 2 = 1.5
'''

import math
import random


#Input usuario , Rango incial y rango final .
r_i = int(input('Ingrese el rango inicial para generar aletorios que sean > 0 :'))
r_f = int(input('Ingrese el rango final para generar aletorios que sean > 0 :'))

#Funcion generadora de numeros aletorios, en el rango de n 
#Yo aplique que los numeros generados podrian ser aletorios y en un rango dado.
randoms = list(random.randint(r_i,r_f) for r_i in range(r_i,r_f)) #Genera numeros apartir del r_i  >= r_f y apartir de la cantidad de elemtos entre el rango genera los elementos.
print("Lista generada aletoriamente :",list(randoms), end=' ') #Imprime la lista de los numeros generados

'''
Serie a calcular
            (2n)!
            (n + 1)!n!
'''
serie =  (lambda n:  math.factorial( 2*n ) / (math.factorial(n + 1) * math.factorial(n))) #calculamos la serie con la funcion lambda, math.factorial() de la libreria de math en python ,  nos calcula el factorial de un elemnto, esto es programacio funcional,  lo implemente con la razon de que sea mas eficiente y sencillo de entender este calculo
calcular_serie = list((map(serie, randoms))) #aplicamos la serie sobre la lista de numeros generados por medio de map que como parametro recibe una funcion de calculo y un parametro de tipo lista en este caso.

#imprimimos la serie 
print("Serie calculada :",(calcular_serie))