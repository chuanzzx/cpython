import self
from .foo import test

expected_result = {'test.lazyimports.split_fromlist.foo', 'test.lazyimports.split_fromlist.foo.bar'}
result = test()
self.assertEqual(result, expected_result)
