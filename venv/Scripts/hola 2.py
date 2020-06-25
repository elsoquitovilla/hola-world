numero1=int(input("ingresa un numero 1; "))
numero2=int(input("ingresa un numero 2; "))

if numero1>numero2:
    print(f"el numero {numero1} es mayor, el numero {numero2} es el menor ")
elif numero2>numero1:
        print(f"el numero {numero2} es mayor, el numero {numero1} es el menor ")
else:
    print("son iguales")