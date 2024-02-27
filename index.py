saldo = 0
limite = 500
extrato = ""
numeros_saque = 0
LIMITE_SAQUE = 3

def deposito() :
    vlrDeposito = 0

    while True:
        vlrDeposito = float(input("Digite o valor do deposito: "))
        if(vlrDeposito <= 0) :
            print("Digite um valor maior que 0")
            vlrDeposito = 0
        else:
            return vlrDeposito
        
def saque() :
    vlrSaque = float(input("Quanto voce quer sacar ? "))
    if vlrSaque > limite :
        print("Valor maximo de 500 ultrapassado. ")
        return 0   
    elif (vlrSaque > saldo and (saldo <=0)):
        print(print("Voce não tem saldo suficiente "))
        return 0    
    else :
        return vlrSaque 


menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato    
    [4] Sair
  """


while True:
    
    opcao = input(menu)
    
    if opcao == "1" :
            print("Depositar")
            valor_deposito = deposito()
            saldo += valor_deposito
            extrato += "Deposito: " + str(valor_deposito) + "\n"
         

    elif opcao == "2" :
        print("Sacar")
        if(saldo>0):
            valor_saque = float(saque())
            if ((valor_saque > 0 )and numeros_saque < LIMITE_SAQUE) :
                saldo -= valor_saque
                extrato += "Saque:    " + str(valor_saque) + "\n"
                numeros_saque += 1
            else:
                print("numeros de saque diarios excedidos")     
        else :
             print("Sua conta esta zerada") 
             
    elif opcao =="3" : 
        print("Extrato") 
        print(extrato)
    elif opcao == "4" :
        print("Sair")
        break
    else :
        print("Digite uma opcao valida")



