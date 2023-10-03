diaSolicitado = input("Dime el dia de la semana: ")


if (diaSolicitado == "lunes"):
    print("Buenos dias!")
elif( diaSolicitado == "viernes"):
    print("Casi fin de semana!")
elif(diaSolicitado == "sabado" or diaSolicitado == "domingo"):
    print("Fin de Semana")
else:
    print("Dia no valido")
    