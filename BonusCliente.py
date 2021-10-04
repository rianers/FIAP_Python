print("**********************************************************************************\n"
      "* CAP 2 - QUANDO A MÁQUINA COMEÇA A TOMAR DECISÕES - LISTA DE EXERCÍCIOS COM IFS * \n"
      "********************************************************************************** \n")
print("Esse programa calcula e fornece o valor do bônus do cliente. \n")
tipoAssinatura = int(input("Por favor, digite o número correspondente ao seu tipo de assinatura \n"
                       "Suas opções: \n"
                       "1 - Basic \n"
                       "2 - Silver \n"
                       "3 - Gold \n"
                       "4 - Platinum \n"))
numero = 5

if(tipoAssinatura < numero and tipoAssinatura > 0):
    faturamento = float(input("Agora, informe o seu faturamento anual (utilize pontos no lugar da vírgula) \n"))
if(tipoAssinatura == 1):
    bonus = faturamento * 0.3
    print("O seu bônus é de R${:.2f}".format(bonus))
elif(tipoAssinatura == 2):
    bonus = faturamento * 0.2
    print("O seu bônus é de R${:.2f}".format(bonus))
elif(tipoAssinatura == 3):
    bonus = faturamento * 0.1
    print("O seu bônus é de R${:.2f}".format(bonus))
elif(tipoAssinatura == 4):
    bonus = faturamento * 0.05
    print("O seu bônus é de R${:.2f}".format(bonus))
else:
    print("Favor digitar um número válido.")

