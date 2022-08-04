import _imp
import importlib
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
    def test_lazy_imports(self):
        for name, lazy in (
            ("test.lazyimports.dict_update", True),
            ("test.lazyimports.circular_import", True),
            ("test.lazyimports.circular_import", False),
            ("test.lazyimports.deferred_resolve_failure", True),
            ("test.lazyimports.deferred_resolve_failure", False),
            ("test.lazyimports.split_fromlist", True),
            ("test.lazyimports.importlib_apis.enable_lazy_imports_at_runtime", False),
            ("test.lazyimports.attribute_side_effect", True),
            ("test.lazyimports.attribute_side_effect", False),
            ("test.lazyimports.importlib_apis.set_lazy_imports_excluding_list", True),
            ("test.lazyimports.importlib_apis.set_lazy_imports_excluding_cb", True),
            ("test.lazyimports.importlib_apis.set_lazy_imports_excluding_cb_list", True),
            ("test.lazyimports.importlib_apis.set_lazy_imports_excluding_list", False),
            ("test.lazyimports.importlib_apis.set_lazy_imports_excluding_cb", False),
            ("test.lazyimports.importlib_apis.set_lazy_imports_excluding_cb_list", False),
            ("test.lazyimports.dict_changes_when_loading", True),
            ("test.lazyimports.dict_changes_when_loading", False),
            ("test.lazyimports.dict_tests", True),
            ("test.lazyimports.from_import_star", True),
            ("test.lazyimports.is_lazy_imports_enabled", True),
            ("test.lazyimports.is_lazy_imports_enabled", False),
            ("test.lazyimports.disable_lazy_imports", True),
            ("test.lazyimports.import_same_name_variable", True),
            ("test.lazyimports.dict_delete", True),
            ("test.lazyimports.reach_max_recursion", True),
            ("test.lazyimports.reach_max_recursion", False),
            ("test.lazyimports.immediate_set_lazy_import", True),
            ("test.lazyimports.immediate_set_lazy_import_global", True),
            ("test.lazyimports.dict_values", True),
            ("test.lazyimports.lazy_side_effects", True),
            ("test.lazyimports.lazy_submodules", True),
        ):
            msg = f"{name}{' (lazy)' if lazy else ' (eager)'}"
            with self.subTest(msg=msg):
                previously = _imp._set_lazy_imports(lazy)
                sys.modules["self"] = self
                try:
                    importlib.import_module(name)
                finally:
                    del sys.modules["self"]
                    _imp._set_lazy_imports(previously)


if __name__ == '__main__':
    unittest.main()
