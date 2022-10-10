def my_decorator(func_to_be_decorated):
    def inner():
        print('Decorating...')
        func_to_be_decorated()
        print('Decorated.')

    return inner


@my_decorator
def square():
    print('gift')


square()
# ret = my_decorator(square)
# ret()
