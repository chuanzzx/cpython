import self
import warnings

vars = {}
vars.update(globals())

result = vars['warnings']

self.assertEqual(result, warnings)
