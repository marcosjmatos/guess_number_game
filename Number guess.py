import random
import math

Upper = int(input("introduzca rango superior: "))
Lower = int(input("introduzca rango inferior: "))

Num_a_adivinar = random.randint(Lower,Upper)

intentos = int(input("cuantas oportunidades de adivinar necesitas?: "))


count = 0


while count < intentos:
    count += 1

    adivinar = int(input("Adivina el numero: "))

    if  Num_a_adivinar == adivinar:
        print("****Felicidades, Ganaste****")
        break
    elif Num_a_adivinar > adivinar:
        print("Intenta con un numero mas alto")
    elif Num_a_adivinar < adivinar:
        print("Intenta con un numero mas bajo")

if count >= intentos:
    print("Perdiste")
    print("el numero era ", Num_a_adivinar)

