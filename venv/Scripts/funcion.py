# solicitar al usuario el ingreso de 2 numeros
# crear funcion que valide:
# si el primer numero es mayor que el segundo, retornar un 1
# si el segundo es mayor que el primero, retornar un -1
# si son iguales retornar un cero
#imprimir el resultado
#utilizar funciones



num1=int(input("ingrese numero uan: "))
num2=int(input("ingrese numero two: "))

def comparacion(num1,num2):
    if (num1>num2):
        return 1

    elif (num2>num1):
        return -1

    else:
        return 0

    #retorno = comparacion(num1,num2)
print ("el valor de retorno es: ", comparacion(num1,num2))

