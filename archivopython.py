
#Crear un nuevo archivo python en cual me permita calcular :
#! Area de un cuadrado
#2 area de un triangulo
#3 area de un rectangulo


figura_geometrica=(input("ingrese figura geometrica: "))
a=int(input("ingrese lado a: "))
b=int(input("ingrese lado b: "))

def comparacion():
    if (figura_geometrica=="cuadrado"):
        area_cuadrado= a*a
        return area_cuadrado

    elif (input==triangulo):
        area_triangulo= (a*b)/2
        return area_triangulo

    elif (input==rectangulo):
        area_rectangulo = a*b
        return area_rectangulo

    #retorno = comparacion(num1,num2)
print ("el valor de retorno es: ", comparacion ())