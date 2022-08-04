import self
if not self._lazy_imports:
    self.skipTest("Test relevant only when running with lazy imports enabled")

import importlib


"""
Test lazy imports
"""
from test.lazyimports.customized_modules import module
self.assertTrue(importlib.is_lazy_import(globals(), "module"))


"""
Test dictionary copy and resolving lazy imports
"""
g = globals()
gcopy = g.copy()
gcopy_resolved = gcopy.copy()
gcopy_resolved.values()  # resolve all elements

self.assertTrue(importlib.is_lazy_import(g, "module"))
self.assertTrue(importlib.is_lazy_import(gcopy, "module"))
self.assertFalse(importlib.is_lazy_import(gcopy_resolved, "module"))


"""
Test | of lazy dictionaries and lazy/non-lazy combinations.
"""
# if `gcopy` and `gcopy_resolved` have the same key
# the value should be `gcopy_resolved[key]`
dict_or_resolved = gcopy | gcopy_resolved
self.assertFalse(importlib.is_lazy_import(dict_or_resolved, "module"))
dict_or_unresolved = gcopy_resolved | gcopy
self.assertTrue(importlib.is_lazy_import(dict_or_unresolved, "module"))


"""
Test merging lazy/non-lazy dictionaries (dict.update()).
"""
gcopy.update(gcopy_resolved)
self.assertFalse(importlib.is_lazy_import(gcopy, "module")) # should be eager
gcopy.update(g)
self.assertTrue(importlib.is_lazy_import(gcopy, "module")) # should be lazy
