# Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python como parte do Bootcamp Santander na DIO.

## Funcionalidades

- **Depósito**: Permite depositar valores positivos na conta
- **Saque**: Permite sacar valores com as seguintes limitações:
  - Máximo de 3 saques por dia
  - Limite de R$500 por saque
  - Verificação de saldo suficiente
- **Extrato**: Exibe o histórico de transições e saldo atual
- **Interface amigável**: Menu interativo com formatação clara

## Como Executar

1. Certifique-se de ter Python instalado (versão 3.6 ou superior)
2. Execute o seguinte comando no terminal:
   ```bash
   python main.py
   ```
3. Siga as instruções do menu interativo

## Uso do Sistema

Ao executar o programa, você verá o seguinte menu:

```
==============================
====== Sistema Bancário ======
==============================
1. Depositar
2. Sacar
3. Extrato
4. Sair
```

- **Depositar**: Digite 1 e informe o valor a ser depositado
- **Sacar**: Digite 2 e informe o valor a ser sacado (respeitando os limites)
- **Extrato**: Digite 3 para visualizar o histórico de transações
- **Sair**: Digite 4 para encerrar o sistema

## Implementação Técnica

- Armazenamento de estado em variáveis globais:
  - `saldo`: Saldo atual da conta
  - `extrato`: Histórico de transações formatado
  - `numero_saques`: Contador de saques diários
- Constantes de configuração:
  - `LIMITE_SAQUES = 3` (limite diário de saques)
  - `limite = 500` (valor máximo por saque)
- Validações de entrada para garantir operações válidas

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
