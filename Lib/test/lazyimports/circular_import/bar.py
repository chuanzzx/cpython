def Bar():
    return "Bar"

from .foo import FooBar

def BarFooBar():
    return FooBar()
