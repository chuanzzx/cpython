# Test the behavior when a module has a sub-module and a variable with the same namings
# Different import/define orderings will expect different results

from test.lazyimports.customized_modules import module_same_name_var_order1
assert(module_same_name_var_order1.bar == "Blah")

import sys
from test.lazyimports.customized_modules import module_same_name_var_order2
assert(module_same_name_var_order2.bar == sys.modules["test.lazyimports.customized_modules.module_same_name_var_order2.bar"])
