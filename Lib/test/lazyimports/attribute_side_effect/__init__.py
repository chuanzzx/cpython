import self
import test.lazyimports.attribute_side_effect.main as main

expected_version = "1.0"
expected_copyright = "Copyright (c) 2001-2022 Python Software Foundation."

self.assertEqual(main.__copyright__, expected_copyright)
self.assertEqual(main.__version__, expected_version)
