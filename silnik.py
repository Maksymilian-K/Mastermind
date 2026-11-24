import random as r


def randomizer(ilosc: int):
    liczba = ""

    for i in range(ilosc):
        liczba += str(r.randint(0, 9))

    return liczba


if __name__ == "__main__":
    print(randomizer(4))
