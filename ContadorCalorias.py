print("*******************************************************************************************\n"
      "* CAP 3 - ANDAR EM CÍRCULOS NÃO É NECESSARIAMENTE RUIM... - LISTA DE EXERCÍCIOS COM LOOPS * \n"
      "******************************************************************************************* \n")
print("Esse programa informa o total de calorias consumidas. \n")

totalCalorias = 0
qtdeAlimentos = int(input("Quantos alimentos você consumiu? "))

for x in range(0, qtdeAlimentos):
    calorias = float(input("Informe a quantidade de calorias do {}º alimento: ".format(x+1)))
    totalCalorias = totalCalorias + calorias
print("{} calorias foram consumidas no total".format(totalCalorias))

