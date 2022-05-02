# peso = int(input("ingresa peso en kg: "))
# altura = int(input("ingresa altura en cm: "))
# altura = altura / 100
# imc = peso / (altura * altura)
# print("IMC : " + str(imc))
# if imc < 20:
#     print("Delgadez")
# if imc >= 20 and imc < 26:
#     print("Normal")
# if imc >= 26 and imc < 30:
#     print("Sobrepeso")

def calcularIMC(peso, alturaEnMetros):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    return imc

def getIMC():
    peso = int(input("ingresa peso en kg: "))
    altura = int(input("ingresa altura en cm: "))
    altura = altura / 100
    imc = peso / (altura * altura)
    print("IMC : " + str(imc))

getIMC()