# Test the lazy imports objects are not exposed when checking the values of dictionaries
import importlib
from test.lazyimports.customized_modules import module
from test.lazyimports.customized_modules.module import *

g = globals().copy()
g_copy1 = g.copy()
g_copy2 = g.copy()
g_copy3 = g.copy()
g_copy4 = g.copy()

def notExposeLazyPrefix(obj_repr):
    return not obj_repr.startswith("<lazy_import ")


# Test dict.values()
for value in g_copy1.values():
    assert(notExposeLazyPrefix(repr(value)))

# Test dict.items()
for key, value in g_copy2.items():
    assert(notExposeLazyPrefix(repr(value)))

# Test iter(dict.values())
it = iter(g_copy3.values())
for value in it:
    assert(notExposeLazyPrefix(repr(value)))

# Test iter(dict.items())
it = iter(g_copy4.items())
for key, value in it:
    assert(notExposeLazyPrefix(repr(value)))

# Test directly getting values by using keys
assert(notExposeLazyPrefix(repr(g["module"])))
assert(notExposeLazyPrefix(repr(g["sub_module1"])))
assert(notExposeLazyPrefix(repr(g["sub_module2"])))
assert(notExposeLazyPrefix(repr(g["sub_module3"])))
