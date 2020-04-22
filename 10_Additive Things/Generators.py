import random
def lottery():
    for i in range(3):
        yield random.randint(1, 10)

    yield random.randint(10, 20)


def test_generators():
    for number_index, random_number in enumerate(lottery()):
        if number_index < 3:
            print("Less than 3")
        else:
            print("Not less than 3")

test_generators()