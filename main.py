nombre = "alex"
edad=34
print("Hola " + nombre + ' y tengo :' + str(edad) + ' años')

nombre2= input('escribe nombre')

print('escribiste : ' + nombre2)

tuEdad= int(input('ingresa edad'))

if edad == tuEdad:
    print("Siii")
else:
    print("Noooo")

if(tuEdad % 2 != 0):
    print("EDAD ES IMPAR")
else:
    print("EDAD ES PAR")