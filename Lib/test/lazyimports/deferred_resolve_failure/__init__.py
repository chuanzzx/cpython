import self
import importlib

if importlib.is_lazy_imports_enabled():
    from . import trigger
else:
    with self.assertRaises(ImportError) as cm:
        from . import trigger
    ex = cm.exception
    self.assertIn("(most likely due to a circular import)", repr(ex))
