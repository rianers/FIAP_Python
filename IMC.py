print("**********************************************************************************\n"
      "* CAP 2 - QUANDO A MÁQUINA COMEÇA A TOMAR DECISÕES - LISTA DE EXERCÍCIOS COM IFS * \n"
      "********************************************************************************** \n")
print("Esse programa calcula e fornece a categoria do seu IMC. \n")

altura = float(input("Informe sua altura em metros e com ponto: "))
peso = float(input("Informe seu peso em kg e com ponto: "))
imc = peso / (altura**2)
desc = ""

if imc < 16:
    desc = "Baixo Peso Grau III"
elif 16 <= imc < 17:
    desc = "Baixo Peso Grau II"
elif 17 <= imc < 18.50:
    desc = "Baixo Peso Grau I"
elif 18.50 <= imc < 25:
    desc = "Peso ideal"
elif 25 <= imc < 30:
    desc = "Sobrepeso"
elif 30 <= imc < 35:
    desc = "Obesidade Grau I"
elif 35 < imc < 40:
    desc = "Obesidade Grau II"
else:
    desc = "Obesidade Grau III"

print("O seu IMC é de {:.2f} e sua categoria é {}.".format(imc, desc))
