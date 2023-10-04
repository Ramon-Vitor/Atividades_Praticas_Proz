saldo = 1000
opcao = int(input ("Informe a opção desejada: "))
if opcao == 1:
 saque = float(input("Informe valor do Saque: "))
 while saque >saldo : 
   print ("saldo insuficiente")
   saque = float(input("Informe valor do Saque: ")) 
 saldo -= saque
 print("O saldo é:", saldo)
elif opcao == 2:
 deposito = float(input("Informe o valor do deposito: "))
 saldo += deposito
 print("O saldo é:", saldo)
elif opcao == 3:
 print("O saldo é:", saldo)
else:
 print ("Opção Invalida") 