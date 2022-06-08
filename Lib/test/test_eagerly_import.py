'''
- Target:
    Add a new sample test that checks Python imports are executed eagerly by default.

- Description:
    We need to confirm one of these two options based on the scenario. Otherwise, this test fails.
        - If it is in default, the imports are executed eagerly.
        - If Lazy Imports is enabled, the imports are NOT executed eagerly.
'''

import os
import sys
import unittest
# import json
import sqlite3

class LazyImportsEnabledChecker:
    def __init__(self):
        self.enabled = self.check_lazy_imports()

    # confirm if Lazy Imports is enabled or not
    def check_lazy_imports(self):
        # lazy imports is not enabled in default
        enabled = False

        # check if Lazy Imports is turned on
        enabled |= self.check_flag()
        enabled |= self.check_env_var()
        return enabled

    # check if the env variable PYTHONLAZYIMPORTSALL is set
    def check_env_var(self):
        env_variables = os.environ
        if "PYTHONLAZYIMPORTSALL" not in env_variables:
            return False

        # check this setting of this env_var
        if env_variables["PYTHONLAZYIMPORTSALL"] == "0":
            return False
        else:
            return True

    # check if -L flag is added to the Python interpreter
    def check_flag(self):
        argvs = sys.argv
        for argv in argvs:
            if argv == "-L" or argv == "-l":
                return True
        return False

    def is_enabled(self):
        return self.enabled


class TestEagerlyImport(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestEagerlyImport, self).__init__(*args, **kwargs)
        self.modules = sys.modules

    def test_json(self):
        # we did not import json, so we should not have these sub-modules
        self.assertFalse("json.encoder" in self.modules)
        self.assertFalse("json.decoder" in self.modules)

    def test_sqlite3(self):
        # we import sqlite3 at the beginning, so we should have sqlite3.dbapi2 in sys.modules
        self.assertTrue("sqlite3.dbapi2" in self.modules)


if __name__ == '__main__':

    lazy_imports_checker = LazyImportsEnabledChecker()

    if lazy_imports_checker.is_enabled():
        # no need to check
        # imports should be lazy
        pass
    else:
        # in default
        # imports should be eagerly
        unittest.main()
