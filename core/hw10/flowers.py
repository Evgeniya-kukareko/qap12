class Flower:
    def __init__(self, name, cost, lifetime):
        self._name = name
        self._cost = cost
        self._lifetime = lifetime

    def __str__(self):
        return f"{self._name} (${self._cost}, {self._lifetime} days)"

    def get_cost(self):
        return self._cost

    def get_lifetime(self):
        return self._lifetime


class Rose(Flower):
    def __init__(self, cost):
        super().__init__("Rose", cost, 5)


class Lily(Flower):
    def __init__(self, cost):
        super().__init__("Lily", cost, 7)


class Daisy(Flower):
    def __init__(self, cost):
        super().__init__("Daisy", cost, 3)


class Bouquet:
    def __init__(self, flowers):
        self._flowers = flowers

    def get_total_cost(self):
        return sum([flower.get_cost() for flower in self._flowers])

    def get_average_lifetime(self):
        return sum([flower.get_lifetime() for flower in self._flowers]) / len(self._flowers)

    def sort_by_cost(self):
        self._flowers = sorted(self._flowers, key=lambda flower: flower.get_cost())

    def has_flower(self, flower_name):
        for flower in self._flowers:
            if flower._name.lower() == flower_name.lower():
                return True
        return False

    def __str__(self):
        return ", ".join([str(flower) for flower in self._flowers])


rose1 = Rose(10)
rose2 = Rose(12)
rose3 = Rose(14)
lily1 = Lily(8)
daisy1 = Daisy(5)

flowers = [rose1, rose2, rose3, lily1, daisy1]

bouquet = Bouquet(flowers)
print(bouquet)

print(bouquet.get_total_cost())
print(bouquet.get_average_lifetime())
bouquet.sort_by_cost()
print(bouquet)

print(bouquet.has_flower("Lily"))
print(bouquet.has_flower("Flower"))
