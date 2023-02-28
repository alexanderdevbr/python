import classAnimal

class Gato(classAnimal.Animal):
    def __init__(self, nome, cor) -> None:
        super().__init__(nome, cor)