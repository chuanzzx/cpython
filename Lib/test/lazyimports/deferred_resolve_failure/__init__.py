import self
import importlib

if importlib.is_lazy_imports_enabled():
    import test.lazyimports.deferred_resolve_failure.main
else:
    with self.assertRaises(ImportError) as cm:
        import test.lazyimports.deferred_resolve_failure.main
    ex = cm.exception
    self.assertIn("(most likely due to a circular import)", repr(ex))
