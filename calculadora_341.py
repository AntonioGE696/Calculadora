print("Holaa")
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    if b == 0:
        print("Error, no se puede dividir por cero")
  
    else:
        b != 0
        return a/b


while True:

    opc = int(input("1.-Sumar, 2.-Restar, 3.-Multiplicar, 4.-Dividir, 5.-Salir:  "))
    


    if opc == 1:
        a = int(input("Ingrese primer número: "))
        b = int(input("Ingrese segundo número: "))

        print(suma(a,b))

    if opc == 2:
        a = int(input("Ingrese primer número: "))
        b = int(input("Ingrese segundo número: "))

        print(resta(a,b))

    if opc == 3:
        a = int(input("Ingrese primer número: "))
        b = int(input("Ingrese segundo número: "))

        print(multi(a,b))

    if opc == 4:
        a = int(input("Ingrese primer número: "))
        b = int(input("Ingrese segundo número: "))

        print(divi(a,b))

    if opc == 5:
        break

    input("Apriete ENTER para seguir")


        


