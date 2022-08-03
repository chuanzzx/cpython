import self
import importlib

from . import foo

importlib.set_lazy_imports(excluding=["test.lazyimports.immediate_set_lazy_import"])

from . import bar

self.assertTrue(importlib.is_lazy_import(globals(), "foo"))
self.assertFalse(importlib.is_lazy_import(globals(), "bar"))
