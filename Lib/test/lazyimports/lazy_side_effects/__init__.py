import self

import test.lazyimports.lazy_side_effects.foo.bar
from test.lazyimports.lazy_side_effects.foo import baz
import test.lazyimports.lazy_side_effects.foo as f

self.assertEqual(f.bar.Bar, "Bar")

with self.assertRaises(AttributeError):
    print(f.baz.Baz)
