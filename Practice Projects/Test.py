import inspect


def test(a, b):
    pass


print(inspect.getfullargspec(test))
