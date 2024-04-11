import datetime

# Lista para armazenar os registros de transação
extrato = []
limite_diario = 500.00  # Limite de saque diário
limite_saques_diario = 3  # Número máximo de saques por dia
saques_realizados_hoje = 0  # Contador de saques realizados hoje
valor_total_saque_hoje = 0.00  # Valor total de saques realizados hoje

saldo = 0

def ver_saldo():
    print(f"Seu saldo atual é: R${saldo:.2f}")

def sacar(valor):
    global saldo, limite_diario, limite_saques_diario, saques_realizados_hoje, valor_total_saque_hoje

    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return

    if valor > limite_diario:
        print("Limite de saque diário excedido.")
        return
    elif saques_realizados_hoje >= limite_saques_diario:
        print("Número máximo de saques por dia atingido.")
        return
    elif (valor_total_saque_hoje + valor) > limite_diario:
        print("Limite de saque diário excedido.")
        return

    saldo -= valor
    data_e_hora = datetime.datetime.now()
    registro = {"Data": data_e_hora, "Valor": valor, "Tipo": "Saque"}
    extrato.append(registro)
    saques_realizados_hoje += 1
    valor_total_saque_hoje += valor
    print(f"Saque de R${valor:.2f} realizado com sucesso!")
    print(f"Seu novo saldo é: R${saldo:.2f}")

def depositar(valor):
    global saldo
    saldo += valor
    data_e_hora = datetime.datetime.now()
    registro = {"Data": data_e_hora, "Valor": valor, "Tipo": "Depósito"}
    extrato.append(registro)
    print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    print(f"Seu novo saldo é: R${saldo:.2f}")

def ver_extrato():
    print("\nVer Extrato:")
    for registro in extrato:
        tipo_transacao = registro["Tipo"]
        if tipo_transacao == "Depósito":
            print(f"Data: {registro['Data']}, Tipo: Depósito, Valor: R${registro['Valor']:.2f}")
        elif tipo_transacao == "Saque":
            print(f"Data: {registro['Data']}, Tipo: Saque, Valor: R${registro['Valor']:.2f}")

def resetar_limite_diario():
    global saques_realizados_hoje, valor_total_saque_hoje
    saques_realizados_hoje = 0
    valor_total_saque_hoje = 0.00

def main():
    while True:
        print("\nBem-vindo ao seu banco digital!")
        print("1. Ver Saldo")
        print("2. Fazer um depósito")
        print("3. Fazer um saque")
        print("4. Ver o extrato")
        print("5. Sair")

        opcao = input("Escolha uma opção (1, 2, 3, 4 ou 5): ")
        if opcao == "1":
            ver_saldo()
        elif opcao == "2":
            valor = float(input("Informe o valor do depósito: R$"))
            depositar(valor)
        elif opcao == "3":
            valor = float(input("Informe o valor do saque: R$"))
            sacar(valor)
        elif opcao == "4":
            ver_extrato()
        elif opcao == "5":
            print("Obrigado por usar o banco digital. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente...")

        # Verifica se mudou o dia, para resetar o limite diário de saques
        hoje = datetime.datetime.now().date()
        if not extrato:
            resetar_limite_diario()
        elif extrato[-1]["Data"].date() != hoje:
            resetar_limite_diario()

if __name__ == "__main__":
    main()
