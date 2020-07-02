numero_par=[]
numero_impar=[]

for num in range(1,11):
    if (num%2==0):
        numero_par.append(num)
    else:
        numero_impar.append(num)

print("numeros pares",numero_par)
print("numeros impares",numero_impar)

numero_par[0:] = [1,3,5,7,9]
numero_impar[0:] = [2,4,6,8,10]

print("remplazar bloque de contenido", numero_par,numero_impar)