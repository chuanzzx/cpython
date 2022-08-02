import importlib

from . import foo

from . import excluding
excluding

from . import bar

assert(importlib.is_lazy_import(globals(), "foo"))
assert(not importlib.is_lazy_import(globals(), "bar"))
