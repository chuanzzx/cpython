import importlib

def disable_lazy_imports():
    importlib.set_lazy_imports(False)

assert(importlib.is_lazy_imports_enabled() == True)
disable_lazy_imports()
assert(importlib.is_lazy_imports_enabled() == False)
