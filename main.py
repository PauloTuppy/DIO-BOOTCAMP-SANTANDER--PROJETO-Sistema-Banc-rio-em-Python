saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def main():
    global saldo, extrato, numero_saques
    
    while True:
        print("\n" + "=" * 30)
        print(" Sistema Bancário ".center(30, "="))
        print("=" * 30)
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("\nSelecione uma opção: ")
        
        if opcao == "1":
            valor = float(input("Valor do depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido! O valor deve ser positivo.")
                
        elif opcao == "2":
            if numero_saques >= LIMITE_SAQUES:
                print("Limite diário de saques atingido!")
                continue
                
            valor = float(input("Valor do saque: R$ "))
            
            if valor > saldo:
                print("Saldo insuficiente!")
            elif valor > limite:
                print(f"Valor excede o limite por saque de R$ {limite:.2f}!")
            elif valor <= 0:
                print("Valor inválido! O valor deve ser positivo.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                
        elif opcao == "3":
            print("\n" + "=" * 30)
            print(" EXTRATO ".center(30, "="))
            print("=" * 30)
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            print("=" * 30)
            
        elif opcao == "4":
            print("Saindo do sistema...")
            break
            
        else:
            print("Opção inválida! Por favor selecione uma opção válida.")

if __name__ == "__main__":
    main()
