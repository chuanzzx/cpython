import sys
from . import bar, baz

def test():
    bar
    return set(m for m in sys.modules if m.startswith("test.lazyimports.split_fromlist."))
