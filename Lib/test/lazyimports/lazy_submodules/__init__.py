import self
import sys

import test.lazyimports.lazy_submodules
import test.lazyimports.lazy_submodules.foo.bar as bar
import test.lazyimports.lazy_submodules.foo.baz as baz

bar.Bar

self.assertIn("test.lazyimports.lazy_submodules.foo.bar", sys.modules)
self.assertNotIn("test.lazyimports.lazy_submodules.foo.baz", sys.modules)

import test.lazyimports.lazy_submodules.waldo.fred as fred
self.assertEqual(test.lazyimports.lazy_submodules.waldo.Waldo, "Waldo")
