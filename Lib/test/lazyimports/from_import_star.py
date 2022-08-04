import self
if not self._lazy_imports:
    self.skipTest("Test relevant only when running with lazy imports enabled")

import importlib

"""
Verify `from foo import *`, imported names that are lazy in `foo` should still be lazy.
"""

from test.lazyimports.customized_modules.module import *

self.assertTrue(importlib.is_lazy_import(globals(), "sub_module1"))
self.assertTrue(importlib.is_lazy_import(globals(), "sub_module2"))
self.assertTrue(importlib.is_lazy_import(globals(), "sub_module3"))
self.assertFalse(importlib.is_lazy_import(globals(), "direct_value"))
