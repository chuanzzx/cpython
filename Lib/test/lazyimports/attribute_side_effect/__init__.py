import self
import test.lazyimports.attribute_side_effect.trigger as attribute_side_effect
import test.lazyimports.attribute_side_effect.structures as structures

expected_copyright = "Copyright 2022 Meta Platforms, Inc."
expected_version = "1.0"
expected_struc_obj = "<class 'test.lazyimports.attribute_side_effect.structures.TestStructure'>"

self.assertEqual(attribute_side_effect.__copyright__, expected_copyright)
self.assertEqual(attribute_side_effect.__version__, expected_version)
self.assertEqual(repr(structures.TestStructure), expected_struc_obj)
