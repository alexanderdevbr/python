class Animal():
    def __init__(self, nome, cor) -> None:
        self.__nome = nome
        self.__cor = cor

    def comer(self):
        print(f"O {self.__nome} está comendo")