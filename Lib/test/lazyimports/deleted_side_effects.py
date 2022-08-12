"""
Test deleting a module from a dict
"""
import self
import sys

import test.lazyimports.customized_modules.foo as foo

import test.lazyimports.customized_modules.foo.bar.baz

first_bar = test.lazyimports.customized_modules.foo.bar

del sys.modules["test.lazyimports.customized_modules.foo.bar"]

import test.lazyimports.customized_modules.foo.bar.thud

second_bar = test.lazyimports.customized_modules.foo.bar

self.assertIn("test.lazyimports.customized_modules.foo.bar", set(sys.modules))
sys_modules_bar = sys.modules["test.lazyimports.customized_modules.foo.bar"]

self.assertIsNot(first_bar, second_bar)
self.assertIsNot(sys_modules_bar, first_bar)
self.assertIs(sys_modules_bar, second_bar)

self.assertIn("baz", dir(first_bar))
self.assertNotIn("thud", dir(first_bar))

self.assertNotIn("baz", dir(second_bar))
self.assertIn("thud", dir(second_bar))
