import self
import importlib

def disable_lazy_imports():
    importlib.set_lazy_imports(False)

self.assertTrue(importlib.is_lazy_imports_enabled())

disable_lazy_imports()

self.assertFalse(importlib.is_lazy_imports_enabled())
