pokemones =[['charmander',1],
           ['charmileon',2],
           ['charizard',3]]

for pokemon in pokemones:
    print("{:10}: {:2}".format(pokemon[0],pokemon[1]))
#modificacion de parametros
pokemones[2][1] = 22

print(pokemones[2][1])

pokemones.append(['squire'])

pokemones[3].append(4)
for pokemon in pokemones:
    print("{:10}: {:2}".format(pokemon[0],pokemon[1]))

"""for pokemon in pokemones:
    print("{:10}: {:2}".format(pokemon[0],pokemon[1]))

print ("****************** otro **********************")

figuras = [["Cuadrados",6,[3,1]],
           ["circulos",5,[1,2]],
           ["triangulos",4,[2,2]],
           ["rectangulos",3,[4,3]]]

figuras[0][1]=5
figuras[0][2]=[1,3]
figuras[3][2][0]=2
print(figuras)
for form in figuras:
    print("{:14}: {:2}. Columna: {}. Fila: {}.".format(form[0],form[1],form[2][0],form[2][1]))

print ("****************** segundo **********************")

cajon1=[]
cajon2=[]

for cajonera1 in cajon1:
    print()

mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)

print(mi_tupla[-4])"""

