class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado na conta {self.numero_conta}. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado na conta {self.numero_conta}. Saldo atual: R${self.saldo}")
        else:
            print(f"Saldo insuficiente na conta {self.numero_conta}. Saque cancelado.")

    def transferir(self, conta_destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor} realizada da conta {self.numero_conta} para a conta {conta_destino.numero_conta}.")
        else:
            print(f"Saldo insuficiente na conta {self.numero_conta}. Transferência cancelada.")

    def consultar_saldo(self):
        print(f"Saldo na conta {self.numero_conta}: R${self.saldo}")


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        print(f"Conta {numero_conta} não encontrada.")
        return None



def exibir_menu():
    print("----- Menu -----")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Transferir")
    print("5. Consultar saldo")
    print("6. Sair")



meu_banco = Banco("Meu Banco")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero_conta = input("Digite o número da conta: ")
        nome_titular = input("Digite o nome do titular da conta: ")
        saldo_inicial = float(input("Digite o saldo inicial da conta: "))

        conta = ContaBancaria(numero_conta, nome_titular, saldo_inicial)
        meu_banco.adicionar_conta(conta)
        print("Conta criada com sucesso!")

    elif opcao == "2":
        numero_conta = input("Digite o número da conta: ")
        valor = float(input("Digite o valor a ser depositado: "))

        conta = meu_banco.buscar_conta(numero_conta)
        if conta:
            conta.depositar(valor)

    elif opcao == "3":
        numero_conta = input("Digite o número da conta: ")
        valor = float(input("Digite o valor a ser sacado: "))

        conta = meu_banco.buscar_conta(numero_conta)
        if conta:
            conta.sacar(valor)

    elif opcao == "4":
        numero_conta_origem = input("Digite o número da conta de origem: ")
        numero_conta_destino = input("Digite o número da conta de destino: ")
        valor = float(input("Digite o valor a ser transferido: "))

        conta_origem = meu_banco.buscar_conta(numero_conta_origem)
        conta_destino = meu_banco.buscar_conta(numero_conta_destino)
        if conta_origem and conta_destino:
            conta_origem.transferir(conta_destino, valor)

    elif opcao == "5":
        numero_conta = input("Digite o número da conta: ")

        conta = meu_banco.buscar_conta(numero_conta)
        if conta:
            conta.consultar_saldo()

    elif opcao == "6":
        print("Obrigado por usar nosso sistema bancário. Volte sempre!")
        break

    else:
        print("Opção inválida. Digite novamente.")