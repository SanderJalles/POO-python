class Estacionamento:
    def __init__(self):
        self.vagas = [None] * 10
        self.pagamento = {}

    def estacionar(self, veiculo):
        for i in range(len(self.vagas)):
            if self.vagas[i] is None:
                self.vagas[i] = veiculo
                print(f"Veículo {veiculo} estacionado na vaga {i + 1}")
                return
        print("Desculpe, não há vagas disponíveis.")

    def pagar_estacionamento(self, veiculo):
        self.pagamento[veiculo] = True
        print(f"Veículo {veiculo} pagou o estacionamento.")

    def sair(self, veiculo):
        if veiculo in self.vagas:
            if self.pagamento.get(veiculo):
                self.vagas[self.vagas.index(veiculo)] = None
                print(f"Veículo {veiculo} saiu do estacionamento.")
            else:
                print(f"Veículo {veiculo} não pagou o estacionamento.")
        else:
            print(f"Veículo {veiculo} não está estacionado aqui.")

    def vagas_disponiveis(self):
        count = 0
        for vaga in self.vagas:
            if vaga is None:
                count += 1
        return count

    def imprimir_vagas(self):
        for i in range(len(self.vagas)):
            vaga = self.vagas[i]
            if vaga is None:
                print(f"Vaga {i + 1}: Vaga vazia")
            else:
                print(f"Vaga {i + 1}: {vaga}")



estacionamento = Estacionamento()

estacionamento.estacionar("Carro1")
estacionamento.estacionar("Carro2")
estacionamento.estacionar("Moto1")

estacionamento.imprimir_vagas()


estacionamento.pagar_estacionamento("Carro1")
estacionamento.sair("Carro2")
estacionamento.sair("Moto1")

estacionamento.imprimir_vagas()

