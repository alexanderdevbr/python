import classAnimal

class Cachorro(classAnimal.Animal):
    def __init__(self, nome, cor) -> None:
        super().__init__(nome, cor)