class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self, _id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
