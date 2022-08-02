import importlib
import unittest
import warnings

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
    def test_dict_update(self):
        with importlib._lazy_imports(True):
            mod = import_fresh_module("test.lazyimports.dict_update")
            self.assertEqual(mod.result, warnings)

    def test_deferred_resolve_failure(self):
        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.deferred_resolve_failure")

        with importlib._lazy_imports(False):
            with self.assertRaises(ImportError) as cm:
                import_fresh_module("test.lazyimports.deferred_resolve_failure")
            ex = cm.exception
            self.assertIn("(most likely due to a circular import)", repr(ex))

    def test_split_fromlist(self):
        expected_result = {'test.lazyimports.split_fromlist.foo', 'test.lazyimports.split_fromlist.foo.bar'}
        with importlib._lazy_imports(True):
            mod = import_fresh_module("test.lazyimports.split_fromlist")
            self.assertEqual(mod.result, expected_result)

    def test_enable_lazy_imports_at_runtime(self):
        with importlib._lazy_imports(False):
            import_fresh_module("test.lazyimports.importlib_apis.enable_lazy_imports_at_runtime")

    def test_attribute_side_effect(self):
        with importlib._lazy_imports(False):
            import_fresh_module("test.lazyimports.attr_side_effect")

        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.attr_side_effect")

    def test_set_lazy_imports_excluding(self):
        with importlib._lazy_imports(False):
            import_fresh_module("test.lazyimports.importlib_apis.set_lazy_imports_excluding_list")
            import_fresh_module("test.lazyimports.importlib_apis.set_lazy_imports_excluding_cb")
            import_fresh_module("test.lazyimports.importlib_apis.set_lazy_imports_excluding_cb_list")

        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.importlib_apis.set_lazy_imports_excluding_list")
            import_fresh_module("test.lazyimports.importlib_apis.set_lazy_imports_excluding_cb")
            import_fresh_module("test.lazyimports.importlib_apis.set_lazy_imports_excluding_cb_list")

    def test_dict_changes_when_loading(self):
        with importlib._lazy_imports(False):
            import_fresh_module("test.lazyimports.check_dict_changes_when_loading")

        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.check_dict_changes_when_loading")

    def test_dict(self):
        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.dict_tests")

    def test_from_import_star(self):
        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.from_import_star")

    def test_is_lazy_imports_enabled(self):
        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.is_lazy_imports_enabled")

        with importlib._lazy_imports(False):
            import_fresh_module("test.lazyimports.is_lazy_imports_enabled")

    def test_disable_lazy_imports(self):
        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.disable_lazy_imports")

    def test_import_module_has_same_name_var_as_submodule_name(self):
        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.import_same_name_variable")

    def test_dict_delete(self):
        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.dict_delete")

    def test_reach_max_recursion(self):
        with importlib._lazy_imports(False):
            import_fresh_module("test.lazyimports.reach_max_recursion")

        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.reach_max_recursion")

    def test_immediate_set_lazy_import(self):
        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.immediate_set_lazy_import")

        with importlib._lazy_imports(True):
            import_fresh_module("test.lazyimports.immediate_set_lazy_import_global")


if __name__ == '__main__':
    unittest.main()
