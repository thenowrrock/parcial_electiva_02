
#Autores Juan David Jimenez 

#El dia de hoy 23/10/2021,  tuve un accidente :c  y tengo un trauma en la cabeza , tambien esto me hizo bajar el rendimiento

'''
•Escriba un programa que basado en 3 palabras dadas por
el usuario construya un crucigrama. El objetivo es
maximizar en el crucigrama el número de letras en común
entre las palabras.
Condiciones:

• El tamaño del crucigrama no está predeterminado y
puede ser el resultado de la optimización solicitada.
• El tamaño de las palabras no está predeterminado
• La orientación de las palabras puede ser cualquier
dirección horizontal o vertical



•Punto No. 3
Valor del punto 3 = 2.5


'''
#Como se abordo el problema:
'''
En primera parte me imagine que deberiamos de crear un espacio en donde se deberian ver las palabras ingresadas y que mejor forma
que tener una lista de matrices en la cual pudieramos  movernos desde la posicion x en  direcciones  <-> y que 
en la posicion y pudieramos ir  en las direcciones abajo,arriba, ya en parte se puedemos vizualizar la solucion,
pero aqui es donde enfrentamos el problema de las palabras y sus ocurrencias entre ellas, para formar el crucigrama, para 
darle una implementacion a esto analice que cada palabra tiene un tamaño de caracteres que irian en la matriz,pero tambien deberiamos 
deberiamos de guardar la posicion de los caractesres en la matriz , para poder ir moviendonos en la matriz[x][y].

Bueno al ver que podemos movernos en la matriz gracias al saber en que posicion esta cada elemento guardado en ella,
definimos que las palabras deberian de filtrarse en corta,mediana,larga, porque esto nos ayudara a darle un tamaño adecuado
a nuestra matriz a la hora de crearla.

Cuando tenemos su tamano ya debemos de ir infiriendo en como las debemos organizar para que sea un crucigrama
en ello analice que debiamos encontra la posicion del caracter que sea semejante al caracter de la segunda palabra 
para poderlo ir ubicando en la matriz  en el caso de : matar , paz 
                                                      #Nuestro programa debe escribir esto en la matriz de la siguiete forma
                                                      
                                                      base la palabra mas larga :  matar 
                                                      base la palabra mas pequeña: paz 
                                                      
                                                      la palabra mas grande se toma  y la agregamos en la matriz:
                                                      
                                                      #Matriz 
                                                      -Agregamos la palabra mas larga.
                                                      
                                                      m a t a r
                                                      
                                                      #Matriz 
                                                      -Aqui es donde debemos saber que posicion vamos a buscar entonces es alli donde trabaja la ocurrencia
                                                      entonces debemos de tener el tamaño de la segunda palabra y de alli buscamos en la primera palabra la 
                                                      primera ocurrencia, entonces quedaria asi:
                                                      
                                                      #Matriz 
                                                      Encontramos que en la poscion x[1] encontramos la ocurrencia en la cual podemos agregar nuestra palabra.
                                                      #Pero como sabemos que nuestra palabra matar esta ocupando la posicon [0][1][2][3][4] ,  no podemos agregar
                                                      la segunda palabra sobre el mismo eje, entonces que hacemos,  buscar la posicon y[1] en el eje vertical de la matriz 
                                                      #Despues de analizado esto vamos aumentando los caracteres de la palabra sobre esa posicion obtenida y agegamos, 
                                                      debemos tener en cuenta que la palabra matar en la poscion x[1] = a ,  ya esta ocupada entonces no es necesario 
                                                      reescribir el caracter entonces como es igual al que ya estamos usando la dejamos y avanzamos y[1] + 1 en la siguiente poscion y[1]
                                                      porque vamos bajando verticalmente y agregamos hasta que termine de recorrer el tamaño de la palabra.
                                                      
                                                      -Quedaria tal que asi :
                                                      
                                                        p
                                                      m a t a r
                                                        z


'''

'''
# Anexo links de  soportes para la creacion de este programa.

https://github.com/thenowrrock/python_para_data_scientists/blob/master/optimizacion_de_codigo.ipynb
https://github.com/andres912/Crucigrama-Python
#Propia documentacion de python 
#Listas en python
#Matrices en python
#strings en python
Tambien con ayuda de mis compañeros de curso se realizo este programa, la participacion de Juan Camilo Bolaños, David Penilla
Que me instruyo y me horiento. 

'''


import os

'''
#Funcion need_lista

Esta encargada de solicitar la informacion de entrada a el usuario por consola.

Solicita las 3 palabras en las que va a trabajar para crear el crucigrama y sacar las comunes letras

Despues de pedirlas las agrega en una lista ordena con cada poscion key

'''
#Funcion need_lista 
def need_lista():
    
    lista = []

    for x in range(3):
        if(x == 0):
            lista.append(input("Escriba la palabra: ").upper())
        else:
            lista.append(input("Escriba la palabra: ").upper())
    
    lista.sort(reverse=True)

    return lista


'''
#funcion ver_en_pantalla
Esta encargada de generar el resultado por consola, conta de 4 parametros para funcionar
fila,columna,matriz,letrasComunes.

Cuando usamos esta funcion debemos de cargar la matriz esto se ve reflejado a que 
vamos trabajando con los caracteres de las palabras  que contiene dicha matriz.

x es la fila en la que nos vamos a mover hacia <-> derecha,izquierda
y  es la columna donde nos vamos a mover hacia ^^ arriba,abajo

Donde se devolvera una matriz[x][y] de el tamañano de las palabras


'''
#funcion ver_en_pantalla
def ver_en_pantalla(fila, columna, matriz, letrasComunes):
    for x in range(fila):
        for y in range(columna):
            print(matriz[y][x], " ", end="")
        print("\n")
    
    print("Numero de letras comunes = ", letrasComunes)
    
    
'''
#funcion crear_matriz   
Esta encargada de crear una matriz recibiendo los parametros de tamaño en x  y tamaño en y

Cuando se usa esta funcion se crea la matriz apartir de una lista que contiene 
el tamaño de la matriz .

Para crear la matriz se debe agregarle un tamaño
tamX tamaño <-> 
tamY tamaño  ^^

Cuando creamos una matriz formamos  algo asi fila * columna:
matriz[4][3] = tamano
|0|1|2|3|
|4|5|6|7|                                          
|4|5|6|7|

Ya obtenido el tamañano de la matriz lo iremos guardando en la lista:
matriz = [], Guardamos su poscion.

En la matriz agreagamos en la  poscion guardada  un espacio " ".

Y me retorna la matriz

'''        
#funcion crear_matriz                
def c_matrix(tamX, tamY):
    matriz = []

    for x in range(tamY):
        matriz.append([])
        for y in range (tamX):
            matriz[x].append(" ")

    return matriz



'''
#Funcion posiciones

Busca una posicion guardada de nuestra matriz comparando la primera poscion x con la anterior que seria y
si esta en x = <-> 
si esta en y = ^^
'''

#Funcion posiciones
def posiciones(lista, letrasComunes):
    posY = 0
    while True:
        if(lista[0][posY] in lista[1]):
            posX = lista[1].find(lista[0][posY])
            letrasComunes = letrasComunes + 2
            break

        posY = posY + 1

    return(letrasComunes, posX, posY)




'''
#funcion insertar_movimiento_horizontal 
Para definir un movimiento en la matriz en x(horizontal) debemos saber la palabra , la matriz , la poscion

Cuando tenemos todo esto, para generar un movimiento en x(horizontal) <->:
Debemos saber el tamaño de la palabra,  esto se consigue por medio de la funcion len()

Teniendo esto, vamos a ir moviendos respecto el tamaño de esa palabra en la matriz
en la poscion x(horizontal)  hasta que llegue a ser igual al tamano de la palabra.

->|0|->|2|->|3|
Me retorna la matriz en la fila con poscion x(horizontal)  <->


'''
#funcion insertar_movimiento_horizontal 
def i_m_h(palabra, matriz, pos):
    for x in range(len(palabra)):
        matriz[pos][x] = palabra[x]
    
    return matriz
'''
#funcion insertar_movimiento_vertical
Para definir un movimiento en la matriz en y(vertical) debemos saber la palabra , la matriz , la poscion

Cuando tenemos todo esto, para generar un movimiento en y(vertical) ^^:
Debemos saber el tamaño de la palabra,  esto se consigue por medio de la funcion len()

Teniendo esto, vamos a ir moviendos respecto el tamaño de esa palabra en la matriz
en la poscion y(vertical)  hasta que llegue a ser igual al tamano de la palabra.
- >|0|
- >|2|
- >|3|

Me retorna la matriz en la columna con poscion y(vertical)  ^^


'''
#funcion insertar_movimiento_vertical 
def i_m_v(palabra, matriz, pos):
    for y in range(len(palabra)):
        matriz[y][pos] = palabra[y]
    
    return matriz



#Funcion lista matrix
def lista_matrix(lista, matriz, posX, posY):
    for x in range(len(lista[0])):
        matriz[posX][x] = lista[0][x]
        
    for y in range(len(lista[1])):
        matriz[y][posY] = lista[1][y]
    return matriz

#Funcion tres palabras
def tres(lista, letrasComunes):
    #matriz = tamano(lista, letrasComunes)
    matriz, fila, columna, letrasComunes = tamano(lista, letrasComunes)
    ver_en_pantalla(fila, columna, matriz, letrasComunes)

#Funcion dos palabras
def dos(lista, letrasComunes):
    matriz = c_matrix(len(lista[0]), len(lista[1]))
    letrasComunes, posX, posY = posiciones(lista, letrasComunes)
    matriz = lista_matrix(lista, matriz, posX, posY)
    ver_en_pantalla(len(lista[0]), len(lista[1]), matriz, letrasComunes)

#Funcion comunes 
def comunes(lista):
    letrasComunes = 0
    for x in range(len(lista)-1, 0, -1):
        for y in range(len(lista)-2, -1, -1):
            if(x != y):
                if(lista[x] in lista[y]):
                    letrasComunes = len(lista[x])
                    lista.pop(x)
                    break
    
    return (lista, letrasComunes)

''''
#Funcion cambio logica if ,else sobre el tamaño de la palabra  mediana,corta,larga
#fila = len(lista[0]) #Por el momento el num de filas

Para evaluar una palabra contaremos los espacios de los carcateres de la string  que tenemos.

Cuando tenemos el numero caracteres de la palabra podemos evaluar las letras comunes.

Esta funcion saca el tamaño de la palabra , toma el tamaño lo compara y busca la posicion de las letras, 
cuando se tiene la posicion de las letras se evalua si es corta,mediana,larga. Y dependiendo de que cumpla 
la palabra se ira agregando en orden de la palabra mas larga hasta la mas corta. 


Cuando ya esta formado todo esto ,  evalua y crea la matriz para las palabras, ya que en la matriz 
conocemos la posicion en la cual se encuentra ese caracter de la palabra y si es corta,mediana,larga. 


esta funcion nos retorna una matriz con palabras , letrasComunes , posiciones

'''
#Funcion cambio logica if ,else sobre el tamaño de la palabra  mediana,corta,larga
def tamano(lista, letrasComunes):
    i = 0
    
    #Tamano de la palabra 
    #Palabra corta
    for w in range(len(lista[1])):
        if(lista[0][w] in lista[1]):
            posX = lista[1].find(lista[0][w])
            letrasComunes = letrasComunes + 1
            posW = w
            break
    

    salir = False
    #palabra mediana
    for z in range(posX+1, len(lista[0])):
        for aux in range(len(lista[2])):
            if(salir):
                break
            if(lista[2][aux] == lista[0][z]):
                posY = z
                posZ = aux
                letrasComunes = letrasComunes + 1
                salir = True

    if(salir == True):
        #Palabra larga
        for z in range(posW+1, len(lista[1])):
            for aux in range(len(lista[2])):
                if(salir):
                    break
                if(lista[2][aux] == lista[1][z]):
                    posY = z
                    posZ = aux
                    letrasComunes = letrasComunes + 2
                    salir = True

        if(salir == True):
            columna = len(lista[1])
            if(posW > posZ):
                mayor = posW
            elif(posW < posZ):
                mayor = posZ
            else:
                mayor = posW

            mayorAuxW = ((posW - len(lista[1])) * -1) + mayor
            mayorAuxZ = ((posZ - len(lista[2])) * -1) + mayor

    else:
        fila = len(lista[0])
        if(posW > posZ):
            mayor = posW
        elif(posW < posZ):
            mayor = posZ
        else:
            mayor = posW

        mayorAuxW = ((posW - len(lista[1])) * -1) + mayor
        mayorAuxZ = ((posZ - len(lista[2])) * -1) + mayor

        if(mayorAuxW > mayorAuxZ):
            matriz = c_matrix(fila, mayorAuxW)
            matriz = i_m_h(lista[0], matriz, posW)
            matriz = i_m_v(lista[1], matriz, posX)
            matriz = i_m_v(lista[2], matriz, posY)
            columna = mayorAuxW

        else:
            matriz = c_matrix(fila, mayorAuxW)
            matriz = i_m_h(lista[0], matriz, posW)
            matriz = i_m_v(lista[1], matriz, posX)
            matriz = i_m_v(lista[2], matriz, posY)
            columna = mayorAuxZ

            if(mayorAuxW > mayorAuxZ):
                matriz = c_matrix(mayorAuxW, columna)
                matriz = i_m_h(lista[0], matriz, posX)
                matriz = i_m_v(lista[1], matriz, posW)
                matriz = i_m_h(lista[2], matriz, posY)
                fila = mayorAuxW

            else:
                matriz = c_matrix(mayorAuxW, columna)
                matriz = i_m_h(lista[0], matriz, posW)
                matriz = i_m_v(lista[1], matriz, posX)
                matriz = i_m_v(lista[2], matriz, posY)
                fila = mayorAuxZ
    
    return (matriz, fila, columna, letrasComunes)


#Inicio programa
lista = need_lista()
print(lista)
lista, letrasComunes = comunes(lista)

if(len(lista) == 3): tres(lista, letrasComunes)
elif(len(lista) == 2):dos(lista, letrasComunes)
else:print(lista[0])
    