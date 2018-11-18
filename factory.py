from abc import ABC, abstractmethod
from datetime import datetime

class Passagem(ABC):
    """docstring for Passagem."""
    def __init__(self, origem, destino, data_hora):
        super(Passagem, self).__init__()
        self.origem = origem
        self.destino = destino
        self.data_hora = data_hora

    @abstractmethod
    def exibe_detalhes(self):
        pass

class PassagemInterEstadual(Passagem):
    """docstring for PassagemInterEstadual."""
    def __init__(self, origem, destino, data_hora):
        super(PassagemInterEstadual, self).__init__(origem, destino, data_hora)

    def exibe_detalhes(self):
        print("Passagem Interestadual")
        print("origem: ", self.origem)
        print("destino: ", self.destino)
        print("data_hora: ", self.data_hora)

class PassagemInterMunicipal(Passagem):
    """docstring for PassagemInterMunicipal."""
    def __init__(self, origem, destino, data_hora):
        super(PassagemInterMunicipal, self).__init__(origem, destino, data_hora)

    def exibe_detalhes(self):
        print("Passagem Intermunicipal")
        print("origem: ", self.origem)
        print("destino: ", self.destino)
        print("data_hora: ", self.data_hora)

class Empresa(ABC):
    """docstring for Empresa."""
    def __init__(self):
        super(Empresa, self).__init__()
        self.passagem = None

    @abstractmethod
    def emite_passagem(self, origem, destino, data_hora):
        pass

class EmpresaInterEstadual(Empresa):
    """docstring for EmpresaInterEstadual."""
    def __init__(self):
        super(EmpresaInterEstadual, self).__init__()

    def emite_passagem(self, origem, destino, data_hora):
        return PassagemInterEstadual(origem, destino, data_hora)

class EmpresaInterMunicipal(Empresa):
    """docstring for EmpresaInterMunicipal."""
    def __init__(self):
        super(EmpresaInterMunicipal, self).__init__()

    def emite_passagem(self, origem, destino, data_hora):
        return PassagemInterMunicipal(origem, destino, data_hora)


if __name__ == '__main__':
    empresa_A = EmpresaInterEstadual()
    empresa_B = EmpresaInterMunicipal()

    passagem_A = empresa_A.emite_passagem("São Paulo", "Belo Horizonte", datetime(2018, 1, 1, 10, 0, 0))
    passagem_B = empresa_B.emite_passagem("São Paulo", "Campinas", datetime(2018, 1, 1, 10, 0, 0))

    passagem_A.exibe_detalhes()
    passagem_B.exibe_detalhes()
