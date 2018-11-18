from abc import ABC, abstractmethod
from datetime import datetime

class PassagemInterEstadual(ABC):
    """docstring for PassagemInterEstadual."""
    def __init__(self, origem, destino, data_hora):
        super(PassagemInterEstadual, self).__init__()
        self.origem = origem
        self.destino = destino
        self.data_hora = data_hora

    @abstractmethod
    def exibe_detalhes(self):
        pass

class PassagemInterMunicipal(ABC):
    """docstring for PassagemInterMunicipal."""
    def __init__(self, origem, destino, data_hora):
        super(PassagemInterMunicipal, self).__init__()
        self.origem = origem
        self.destino = destino
        self.data_hora = data_hora

    @abstractmethod
    def exibe_detalhes(self):
        pass

class ConcretePassagemInterEstadual(PassagemInterEstadual):
    """docstring for PassagemInterEstadual."""
    def __init__(self, origem, destino, data_hora):
        super(ConcretePassagemInterEstadual, self).__init__(origem, destino, data_hora)

    def exibe_detalhes(self):
        print("Passagem Interestadual")
        print("origem: ", self.origem)
        print("destino: ", self.destino)
        print("data_hora: ", self.data_hora)

class ConcretePassagemInterMunicipal(PassagemInterMunicipal):
    """docstring for PassagemInterMunicipal."""
    def __init__(self, origem, destino, data_hora):
        super(ConcretePassagemInterMunicipal, self).__init__(origem, destino, data_hora)

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
    def emite_passagem_intermunicipal(self, origem, destino, data_hora):
        pass

    @abstractmethod
    def emite_passagem_interestadual(self, origem, destino, data_hora):
        pass

class EmpresaXYZ(Empresa):
    """docstring for EmpresaInterEstadual."""
    def __init__(self):
        super(EmpresaXYZ, self).__init__()

    def emite_passagem_intermunicipal(self, origem, destino, data_hora):
        return ConcretePassagemInterEstadual(origem, destino, data_hora)

    def emite_passagem_interestadual(self, origem, destino, data_hora):
        return ConcretePassagemInterMunicipal(origem, destino, data_hora)

if __name__ == '__main__':
    empresa = EmpresaXYZ()

    passagem_A = empresa.emite_passagem_intermunicipal("São Paulo", "Belo Horizonte", datetime(2018, 1, 1, 10, 0, 0))
    passagem_B = empresa.emite_passagem_interestadual("São Paulo", "Campinas", datetime(2018, 1, 1, 10, 0, 0))

    passagem_A.exibe_detalhes()
    passagem_B.exibe_detalhes()
