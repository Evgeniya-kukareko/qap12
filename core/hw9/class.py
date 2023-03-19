class Animal:
    def __init__(self, name, species):
        self._name = name
        self._species = species

    def make_sound(self):
        pass

    def __str__(self):
        return f"{self._name} ({self._species})"

    def get_name(self):
        return self._name

    def get_species(self):
        return self._species


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "dog")

    def make_sound(self):
        return "Bark"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "cat")

    def make_sound(self):
        return "Meow"
