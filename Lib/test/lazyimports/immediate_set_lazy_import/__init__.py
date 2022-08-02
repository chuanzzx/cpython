import importlib

from . import foo

importlib.set_lazy_imports(excluding=["test.lazyimports.immediate_set_lazy_import"])

from . import bar

assert(importlib.is_lazy_import(globals(), "foo"))
assert(not importlib.is_lazy_import(globals(), "bar"))
