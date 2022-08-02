import importlib
previous = importlib.is_lazy_imports_enabled()

with importlib._lazy_imports():
    assert(importlib.is_lazy_imports_enabled() == True)

assert(importlib.is_lazy_imports_enabled() == previous)
