import self
import importlib

if importlib.is_lazy_imports_enabled():
    import test.lazyimports.circular_import.main
else:
    with self.assertRaises(ImportError) as cm:
        import test.lazyimports.circular_import.main
    ex = cm.exception
    self.assertIn("(most likely due to a circular import)", repr(ex))
