print("*******************************************************************************************\n"
      "* CAP 3 - ANDAR EM CÍRCULOS NÃO É NECESSARIAMENTE RUIM... - LISTA DE EXERCÍCIOS COM LOOPS * \n"
      "******************************************************************************************* \n")
print("O algoritmo da sorte de Fibonacci. \n")

numero = int(input("Digite um número: "))

numero_atual = 1
numero_anterior = 0

while numero > numero_atual:
      numero_atual_antigo = numero_atual
      numero_atual = numero_atual + numero_anterior
      numero_anterior = numero_atual_antigo

if(numero == numero_atual):
      print("O número digitado faz parte da sequência.")
else:
      print("O número digitado não faz parte da sequência.")