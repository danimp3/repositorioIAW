numSol1 = int(input("Digame el primer numero: "))
numSol2 = int(input("Digame el segundo numero: "))
numSol3 = int(input("Digame el tercer numero: "))

if (numSol1 > numSol2 and numSol1 > numSol3):
    print("El Primer numero es el mayor de los tres")
elif(numSol2 > numSol3):
    print("El Segundo numero es el mayor de los tres")
    
else:
    print("El Tercer numero es el mayor de los tres")