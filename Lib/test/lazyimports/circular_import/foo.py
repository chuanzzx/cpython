def Foo():
    return "Foo"

from .bar import Bar

def FooBar():
    return Bar()
