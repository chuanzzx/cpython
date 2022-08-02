import sys
old_meta_path = sys.meta_path.copy()
try:
    import test.lazyimports.max_recursion.extern.packaging.markers
finally:
    sys.meta_path[:] = old_meta_path
