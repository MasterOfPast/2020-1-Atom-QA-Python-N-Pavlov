import random
import pytest


@pytest.fixture()
def static_list():
    print("start list")
    yield [1, 2, 3, 4]
    print("end list")


@pytest.fixture(scope="class")
def random_list():
    print("start random list")
    size = random.randint(1, 10)
    yield [random.randint(0, 10) for i in range(size)]
    print("end random list")


@pytest.fixture()
def static_string():
    print("start string")
    yield "Hello world"
    print("end string")


@pytest.fixture(scope='class')
def random_string():
    print("start random string")
    size = random.randint(1, 20)
    string = ""
    for i in range(size):
        string += chr(random.randint(48, 122))
    yield string
    print("end random string")


@pytest.fixture()
def static_int():
    print("start int")
    yield -200
    print("end int")


@pytest.fixture(scope="class")
def random_int():
    print("start random int")
    yield random.randint(-1000, 1000)
    print("end random int")


@pytest.fixture()
def static_dict():
    print("start dict")
    yield {"name": "Name", "login": "login", "password": "password",
           "test": None}
    print("end dict")


@pytest.fixture()
def random_dict():
    print("start random dict")
    yield {a: random.randint(-3, 7) for a in range(10)}
    print("end random dict")


@pytest.fixture()
def static_set():
    print("start set")
    yield {"a", "b", "c", "d", "e"}
    print("end set")
