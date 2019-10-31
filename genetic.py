from string import ascii_lowercase
from random import choices, choice, random, randint
from statistics import mean
from typing import Type, List, Iterable


class Individual:
    mutation_rate: float = 0.1

    def rate(self) -> int:
        raise NotImplementedError

    def mutate(self):
        raise NotImplementedError

    def clone(self) -> "Individual":
        raise NotImplementedError

    def mate(self, other: "Individual") -> "Individual":
        raise NotImplementedError

    def reproduce(self, other: "Individual") -> "Individual":
        if other is self:
            return self.clone()
        return self.mate(other)


class String(Individual):
    goal = "loremipsumdolorsitamet"

    def __init__(self, name):
        self.name = name

    def mutate(self):
        if random() < 0.1:
            self.name = "".join(
                [(l if i == randint(0, len(self.name) - 1) else choice(ascii_lowercase)) for i, l in enumerate(self.name)]
            )

    def rate(self) -> int:
        return sum([1 for l, o in zip(self.name, self.goal) if l == o])

    def __repr__(self):
        return f"{''.join([(l.upper() if l == o else l) for l, o in zip(self.name, self.goal)])} -> {self.rate()}"

    def clone(self) -> "Individual":
        return String(self.name)

    def mate(self, other: "String") -> "Individual":
        name = self.name[0 : randint(0, len(self.name))] + other.name[randint(0, len(other.name)) : len(other.name)]
        return String(name[:22])


Population = List[Individual]


def init_population(individual_type: Type[Individual], pop_size: int, *args, **kwargs) -> Population:
    # noinspection PyArgumentList
    return [individual_type(*args, **kwargs) for _ in range(pop_size)]


def mutate(population: Iterable[Individual]):
    for individual in population:
        individual.mutate()


def reproduce(population: Population) -> Population:
    scores = [max(i.rate(), 1) ** 2 for i in population]
    new_pop_f = choices(population, scores, k=len(population))
    new_pop_m = choices(population, scores, k=len(population))
    return [father.reproduce(mother) for father, mother in zip(new_pop_f, new_pop_m)]


def main():
    population = init_population(String, 5000, "german shepard")
    while True:
        try:
            mutate(population)
            population = reproduce(population)
            scores = [i.rate() for i in population]
            print("-" * 30)
            print(min(scores))
            print(mean(scores))
            print(max(scores))
            pass
        except KeyboardInterrupt:
            break
    print(sorted(population, key=lambda i: i.rate()))


if __name__ == "__main__":
    main()
