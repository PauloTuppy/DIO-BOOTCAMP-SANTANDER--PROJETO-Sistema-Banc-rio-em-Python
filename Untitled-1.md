--- a/sistema_bancario_v1_original.py
+++ b/sistema_bancario_v1_refatorado.py
@@ -1,26 +1,70 @@
 # -*- coding: utf-8 -*-
 
 # Define o menu de opções que será exibido ao usuário
-menu = """
+MENU = """
 ================ MENU ================
 [d]\tDepositar
 [s]\tSacar
 [e]\tExtrato
 [q]\tSair
-=&gt; """
+=> """
 
 # Inicializa as variáveis necessárias para o controle da conta
 saldo = 0
-limite_saque_valor = 500
-extrato = ""
+transacoes = [] # Alterado de string 'extrato' para lista 'transacoes'
 numero_saques = 0
+
+# Constantes do sistema
+LIMITE_SAQUE_VALOR = 500 # Anteriormente 'limite_saque_valor'
 LIMITE_SAQUES_DIARIOS = 3
 
+
+def depositar(saldo_atual, transacoes_atuais):
+    """Realiza a operação de depósito."""
+    print("--- Depósito ---")
+    try:
+        valor_deposito = float(input("Informe o valor do depósito: R$ "))
+
+        if valor_deposito > 0:
+            saldo_atual += valor_deposito
+            # Adiciona a transação à lista formatando o valor
+            transacoes_atuais.append(f"Depósito:\t\tR$ {valor_deposito:10.2f}")
+            print("\nDepósito realizado com sucesso!")
+        else:
+            print("\nOperação falhou! O valor informado é inválido. Deposite apenas valores positivos.")
+    except ValueError:
+        print("\nOperação falhou! Por favor, insira um valor numérico válido.")
+    return saldo_atual, transacoes_atuais
+
+def sacar(saldo_atual, numero_saques_realizados, transacoes_atuais):
+    """Realiza a operação de saque."""
+    print("--- Saque ---")
+    try:
+        valor_saque = float(input("Informe o valor do saque: R$ "))
+
+        excedeu_saldo = valor_saque > saldo_atual
+        excedeu_limite_valor = valor_saque > LIMITE_SAQUE_VALOR
+        excedeu_limite_saques_diarios = numero_saques_realizados >= LIMITE_SAQUES_DIARIOS
+
+        if excedeu_saldo:
+            print(f"\nOperação falhou! Saldo insuficiente. (Saldo atual: R$ {saldo_atual:.2f})")
+        elif excedeu_limite_valor:
+            print(f"\nOperação falhou! O valor do saque excede o limite de R$ {LIMITE_SAQUE_VALOR:.2f} por operação.")
+        elif excedeu_limite_saques_diarios:
+            print(f"\nOperação falhou! Você excedeu o limite de {LIMITE_SAQUES_DIARIOS} saques diários.")
+        elif valor_saque > 0:
+            saldo_atual -= valor_saque
+            numero_saques_realizados += 1
+            transacoes_atuais.append(f"Saque:\t\t\tR$ {valor_saque:10.2f}")
+            print("\nSaque realizado com sucesso!")
+        else:
+            print("\nOperação falhou! O valor informado é inválido.")
+    except ValueError:
+        print("\nOperação falhou! Por favor, insira um valor numérico válido.")
+    return saldo_atual, numero_saques_realizados, transacoes_atuais
+
+def exibir_extrato(saldo_atual, transacoes_atuais):
+    """Exibe o extrato da conta."""
+    print("\n============== EXTRATO ==============")
+    if not transacoes_atuais:
+        print("Não foram realizadas movimentações.")
+    else:
+        for transacao in transacoes_atuais:
+            print(transacao)
+    
+    print(f"\nSaldo atual:\t\tR$ {saldo_atual:10.2f}")
+    print("====================================")
+
 print("Bem-vindo ao nosso sistema bancário!")
 
 # Loop principal do programa, que continua executando até o usuário decidir sair
 while True:
 
     # Exibe o menu e captura a escolha do usuário em minúsculas
-    opcao = input(menu).lower()
+    opcao = input(MENU).lower()
 
     # --- Operação de Depósito ---
     if opcao == "d":
-        print("--- Depósito ---")
-        try:
-            valor_deposito = float(input("Informe o valor do depósito: R$ "))
-
-            # Verifica se o valor do depósito é positivo
-            if valor_deposito &gt; 0:
-                saldo += valor_deposito
-                # Adiciona a transação ao extrato formatando o valor
-                extrato += f"Depósito:\t\tR$ {valor_deposito:.2f}\n"
-                print("\nDepósito realizado com sucesso!")
-            else:
-                print("\nOperação falhou! O valor informado é inválido. Deposite apenas valores positivos.")
-
-        except ValueError:
-            print("\nOperação falhou! Por favor, insira um valor numérico válido.")
-
+        saldo, transacoes = depositar(saldo, transacoes)
 
     # --- Operação de Saque ---
     elif opcao == "s":
-        print("--- Saque ---")
-        try:
-            valor_saque = float(input("Informe o valor do saque: R$ "))
-
-            # Verifica as condições para o saque
-            excedeu_saldo = valor_saque &gt; saldo
-            excedeu_limite_valor = valor_saque &gt; limite_saque_valor
-            excedeu_limite_saques_diarios = numero_saques &gt;= LIMITE_SAQUES_DIARIOS
-
-            if excedeu_saldo:
-                print(f"\nOperação falhou! Saldo insuficiente. (Saldo atual: R$ {saldo:.2f})")
-            
-            elif excedeu_limite_valor:
-                print(f"\nOperação falhou! O valor do saque excede o limite de R$ {limite_saque_valor:.2f} por operação.")
-
-            elif excedeu_limite_saques_diarios:
-                print(f"\nOperação falhou! Você excedeu o limite de {LIMITE_SAQUES_DIARIOS} saques diários.")
-            
-            # Se o valor for positivo e todas as regras forem atendidas
-            elif valor_saque &gt; 0:
-                saldo -= valor_saque
-                numero_saques += 1
-                # Adiciona a transação ao extrato formatando o valor
-                extrato += f"Saque:\t\t\tR$ {valor_saque:.2f}\n"
-                print("\nSaque realizado com sucesso!")
-
-            else:
-                print("\nOperação falhou! O valor informado é inválido.")
-
-        except ValueError:
-            print("\nOperação falhou! Por favor, insira um valor numérico válido.")
-
+        saldo, numero_saques, transacoes = sacar(saldo, numero_saques, transacoes)
 
     # --- Operação de Extrato ---
     elif opcao == "e":
-        print("\n============== EXTRATO ==============")
-        # Verifica se há movimentações no extrato para exibir
-        if not extrato:
-            print("Não foram realizadas movimentações.")
-        else:
-            print(extrato)
-        
-        # Exibe o saldo atual formatado
-        print(f"\nSaldo atual:\t\tR$ {saldo:.2f}")
-        print("====================================")
-
+        exibir_extrato(saldo, transacoes)
 
     # --- Opção de Sair ---
     elif opcao == "q":

