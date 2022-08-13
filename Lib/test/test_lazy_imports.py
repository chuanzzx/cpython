import _imp
import importlib
import os
import sys
import unittest
import warnings

from functools import wraps
from test.support.script_helper import run_python_until_end
from test.support.import_helper import import_fresh_module


class TestLazyImportsSanity(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLazyImportsSanity, self).__init__(*args, **kwargs)

    @unittest.skipIfLazyImportsIsDisabled("Test relevant only when running with lazy imports enabled")
    def test_lazy_imports_is_enabled(self):
        self.assertTrue(importlib.is_lazy_imports_enabled())

    @unittest.skipIfLazyImportsIsEnabled("Test relevant only when running with lazy imports disabled")
    def test_lazy_imports_is_disabled(self):
        self.assertFalse(importlib.is_lazy_imports_enabled())


class LazyImportsTest(unittest.TestCase):
    def setUp(self):
        tests = []
        base = os.path.dirname(__file__)
        for path in os.listdir(os.path.join(base, "lazyimports")):
            if path.startswith("_"):
                continue
            if path.endswith(".py"):
                path = path[:-3]
            name = "test.lazyimports." + path.replace(os.sep, ".")
            tests.append((name, True))
            tests.append((name, False))
        self.tests = tests

    def test_lazy_imports(self):
        original_modules = sys.modules.copy()
        try:
            sys.modules["self"] = self
            for modname in list(sys.modules):
                if modname == "test" or modname.startswith("test."):
                    del sys.modules[modname]
            stripped_modules = sys.modules.copy()

            for test_name, lazy_imports in self.tests:
                msg = f"{test_name}{' (lazy)' if lazy_imports else ' (eager)'}"
                with self.subTest(msg=msg):
                    self._test_name = test_name
                    self._lazy_imports = lazy_imports
                    previously = _imp._set_lazy_imports(lazy_imports)
                    try:
                        importlib.import_module(test_name)
                    finally:
                        _imp._set_lazy_imports(*previously)
                        del self._test_name
                        del self._lazy_imports
                        sys.modules.clear()
                        sys.modules.update(stripped_modules)

        finally:
            sys.modules.clear()
            sys.modules.update(original_modules)


if __name__ == '__main__':
    unittest.main()
