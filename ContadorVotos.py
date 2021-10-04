print("**********************************************************************************\n"
      "* CAP 2 - QUANDO A MÁQUINA COMEÇA A TOMAR DECISÕES - LISTA DE EXERCÍCIOS COM IFS * \n"
      "********************************************************************************** \n")
print("Esse programa informa o resultado da votação para o dia escolhido para a realização das lives. \n")

segunda = int(input("Informe a quantidade de votos para segunda: "))
terca = int(input("Informe a quantidade de votos para terça: "))
quarta = int(input("Informe a quantidade de votos para quarta: "))
quinta = int(input("Informe a quantidade de votos para quinta: "))
sexta = int(input("Informe a quantidade de votos para sexta: "))

if(segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta):
      maiorQtdeVotos = "segunda"
      print("O dia com a maior quantidade de votos foi {} com {} votos.".format(maiorQtdeVotos, segunda))
elif(terca > segunda and terca > quarta and terca > quinta and terca > sexta):
      maiorQtdeVotos = "terça"
      print("O dia com a maior quantidade de votos foi {} com {} votos.".format(maiorQtdeVotos, terca))
elif(quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta):
      maiorQtdeVotos = "quarta"
      print("O dia com a maior quantidade de votos foi {} com {} votos.".format(maiorQtdeVotos, quarta))
elif(quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta):
      maiorQtdeVotos = "quinta"
      print("O dia com a maior quantidade de votos foi {} com {} votos.".format(maiorQtdeVotos, quinta))
elif(sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta):
      maiorQtdeVotos = "sexta"
      print("O dia com a maior quantidade de votos foi {} com {} votos.".format(maiorQtdeVotos, sexta))
else:
      print("Empate!")


