import self
import importlib

from test.lazyimports.importlib_apis.customized_modules import module_is_lazy_import_eager
self.assertFalse(importlib.is_lazy_import(globals(), "module_is_lazy_import_eager"))  # should be eager

importlib.set_lazy_imports()  # enable lazy imports
self.assertTrue(importlib.is_lazy_imports_enabled())

from test.lazyimports.importlib_apis.customized_modules import module_is_lazy_import_lazy
self.assertTrue(importlib.is_lazy_import(globals(), "module_is_lazy_import_lazy"))  # should be lazy

with importlib.eager_imports():
    from test.lazyimports.importlib_apis.customized_modules import module_context_manager_eager
self.assertFalse(importlib.is_lazy_import(globals(), "module_context_manager_eager"))  # should be eager
