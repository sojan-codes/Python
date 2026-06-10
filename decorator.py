def my_decorator(func):
    def wrapper():
        print('This is before Function Runs ')
        func()
        print('This is after the function Runsd')
    return wrapper

def greet():
    print('Hello world')

greet = my_decorator(greet) 


def my_deco(fun):
    def wrapper():
        print('This is the Beginning')
        fun
        print('This is the End')
    return wrapper

def val():
    print('The value is 132')

val = my_deco(val)

val()