import self
import importlib

from . import foo

from . import excluding
excluding

from . import bar

self.assertTrue(importlib.is_lazy_import(globals(), "foo"))
self.assertFalse(importlib.is_lazy_import(globals(), "bar"))
