class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.__nome = nome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__ativo = ativo

    def ativar(self):
        self.__ativo = True
        print(f"{self.__nome} ativado!")

    def desativar(self):
        self.__ativo = False
        print(f"{self.__nome} desativado!")

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


# Main
if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "123.456.789-00", True)
    pessoa2 = Pessoa("Alexander", "M", "901.843.431-00", True)

    pessoa1.desativar()
    pessoa1.nome = "Joaquim"
    pessoa1.ativar()

    print(pessoa2.nome)
