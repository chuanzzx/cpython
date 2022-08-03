import sys

import test.lazyimports.lazy_submodules.foo.bar as bar
import test.lazyimports.lazy_submodules.foo.baz as baz

bar.Bar

assert("test.lazyimports.lazy_submodules.foo.bar" in sys.modules)
assert("test.lazyimports.lazy_submodules.foo.baz" not in sys.modules)
