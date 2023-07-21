#Desafio Criar um sistema bancario em Python

menu = """
1 - Saldo
2 - Extrato
3 - Saque
4 - Transferir
5 - Deposito
0 - Sair

--> Digite sua opção abaixo <--
"""

MAX_SAQUE = 3
LIMITE = 500.0
extrato = []
numero_saque = 0
meu_saldo = 1000.0

while True:

    opcao = input(menu)

    if opcao == "1":
        print(f"Saldo atual: {meu_saldo:.2f}")
    elif opcao == "2":
        for i in extrato:
            print(i)
    elif opcao == "3":
        if MAX_SAQUE > 0:
            saque = float(input("Valor que deseja sacar: "))
            if saque > 500.0:
                print(f"Voce so pode sacar {LIMITE:.2f} diariamente")
            else:
                if saque <= meu_saldo:
                    meu_saldo = meu_saldo - saque
                    print(f"Sacando R${saque:.2f}")
                    extrato.append(saque)
                    print(f"Seu saldo atual é {meu_saldo:.2f}")
                    MAX_SAQUE = MAX_SAQUE - 1
                else:
                    print("Você não tem saldo suficiente")
        else:
            print("Limite de saque atingido")
    elif opcao == "4":
        print("Transferindo")
    elif opcao == "5":
        if deposito > 0:
            deposito = float(input("Digite o valor a ser depositado:"))
            meu_saldo = meu_saldo + deposito
            extrato.append(deposito)
            print(f"Voce depositou {deposito:.2f}")
            print(f"Seu novo saldo é {meu_saldo:.2f}")
        else:
            print("Valor não permitido.")
    else:
        print("Saindo")
        break
