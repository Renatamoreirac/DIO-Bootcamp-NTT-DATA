# Exibe o menu com as opções de operações disponíveis.
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Inicialização de variáveis principais
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite de saque por transação
extrato = ""  # Histórico de transações realizadas
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Limite máximo de saques por dia

# Loop principal que mantém o programa rodando até o usuário sair
while True:

    # Captura a opção escolhida pelo usuário no menu
    opcao = input(menu)

    # Caso a opção seja "d" (Depositar)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        # Verifica se o valor informado é maior que zero
        if valor > 0:
            saldo += valor  # Adiciona o valor ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra o depósito no extrato

        else:
            print("Operação falhou! O valor informado é inválido 😔")  # Exibe mensagem de erro

    # Caso a opção seja "s" (Sacar)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        # Verificações de regras de saque
        excedeu_saldo = valor > saldo  # Verifica se o valor do saque é maior que o saldo
        excedeu_limite = valor > limite  # Verifica se o saque excede o limite permitido
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o número de saques já foi atingido

        # Exibe mensagens de erro de acordo com as verificações feitas
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        # Se o valor for válido e todas as condições estiverem OK
        elif valor > 0:
            saldo -= valor  # Subtrai o valor do saque do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra o saque no extrato
            numero_saques += 1  # Incrementa o número de saques realizados

        else:
            print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro se o valor for inválido

    # Caso a opção seja "e" (Extrato)
    elif opcao == "e":
        # Exibe o extrato detalhado das movimentações ou uma mensagem se não houver transações
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual da conta
        print("==========================================")

    # Caso a opção seja "q" (Sair)
    elif opcao == "q":
        break  # Encerra o loop e o programa

    # Caso o usuário escolha uma opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
