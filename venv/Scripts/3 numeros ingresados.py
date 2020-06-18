#Los números son leídos (ingresados) en forma desordenada, no se validaran números iguales.
#Solo utilizar sentencia if - else - elif
#Comentar cada linea de código, explicando que esta realizando.

#Mostrar tres números ordenados de mayor a menor.

numero1=int(input("ingrese el primer numero: ")) #ingresamos el primero numero junto a su input
numero2=int(input("ingrese el segundo numero: ")) #ingresamos el 2dp numero junto a su input
numero3=int(input("ingrese el tercer numero: ")) #ingresamos el 3er numero junto a su input

if numero1>numero2 and numero1>numero3: #aca se valida que el primer valor sea mayor
    if numero2>numero3: #aca se valida que el segundo numero en su punto critico sea mayor
        print("el mayor es ",numero1," ,el segundo valor es ",numero2," , el tercer valor es ",numero3)

    elif numero2 > numero1 and numero2 > numero3: #aca se valida que el segundo valor sea mayor
        if numero1 > numero3: #aca se valida que el primer numero en su punto critico sea mayor

            print("el mayor es ", numero2, " ,el segundo valor es ", numero1, " , el tercer valor es ", numero3)
        else: # aca se le agrega un sino , de tal modo que si no es un conjunto de variables , va ser el otro por defecto
            print("el mayor es ", numero2, " ,el segundo valor es ", numero3, " , el tercer valor es ", numero1)

else: # en este si no es ninguno de los concadenados anteriormente , sera esta la respuesta por defecto
    if numero2>numero1:
        print("el mayor es ", numero3, " ,el segundo valor es ", numero2, " , el tercer valor es ", numero1)
    if numero1>numero2:
        print("el mayor es ", numero3, " ,el segundo valor es ", numero1, " , el tercer valor es ", numero2)

