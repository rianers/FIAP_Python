print("*******************************************************************************************\n"
      "* CAP 3 - ANDAR EM CÍRCULOS NÃO É NECESSARIAMENTE RUIM... - LISTA DE EXERCÍCIOS COM LOOPS * \n"
      "******************************************************************************************* \n")
print("Esse programa informa a média de cada transação. \n")

transacao = 0
qtdeTransacoes = int(input("Quantas transações financeiras foram realizadas? "))

for x in range(0, qtdeTransacoes):
    valorTransacoes = float(input("Informe o valor da {}ª transação: ".format(x+1)))
    transacao = transacao + valorTransacoes

mediaTransacao = transacao / qtdeTransacoes
print("O valor total das transações foi de R$ {} e a média foi {}.".format(transacao, mediaTransacao))
