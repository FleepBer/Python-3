import math

a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))

delta=b ** 2 -4 * a * c

if delta==0:
    raiz1= (-b + math.sqrt(delta)) / (2 * a)
    print("A única raíz é: ", raiz1)
else:
    if delta <0:
        print("Está equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A primeira raíz é: ", raiz1)
        print("A segunda raíz é: ", raiz2)

