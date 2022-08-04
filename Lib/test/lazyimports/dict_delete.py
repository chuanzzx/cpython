import self
import sys
import importlib

import test.lazyimports.customized_modules.module_delete
test.lazyimports.customized_modules.module_delete
import test.lazyimports.customized_modules.module_delete.module_delete_sub

del sys.modules["test.lazyimports.customized_modules.module_delete"]

import test.lazyimports.customized_modules.module_delete
test.lazyimports.customized_modules.module_delete
import test.lazyimports.customized_modules.module_delete.module_delete_sub

self.assertIn("module_delete_sub", test.lazyimports.customized_modules.module_delete.__dict__)
self.assertTrue(importlib.is_lazy_import(test.lazyimports.customized_modules.module_delete.__dict__, "module_delete_sub"))
