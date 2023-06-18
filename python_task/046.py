def add(function):
    def inner():
        x = function()
        return x + 1
    return inner
    
def cube(function):
    def inner():
        x = function()
        return x * x * x
    return inner
    
def square(function):
    def inner():
        x = function()
        return x * x
    return inner

@square
@cube
@add
def test():
    return 2
test()