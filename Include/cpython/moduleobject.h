#ifndef Py_CPYTHON_MODULEOBJECT_H
#  error "this header file must not be included directly"
#endif

PyAPI_DATA(PyTypeObject) PyLazyImport_Type;

PyAPI_FUNC(PyObject *) PyLazyImportModule_NewObject(PyObject *name, PyObject *globals, PyObject *locals, PyObject *fromlist, PyObject *level);
PyAPI_FUNC(PyObject *) PyLazyImportObject_NewObject(PyObject *from, PyObject *name);
PyAPI_FUNC(PyObject *) PyLazyImport_GetName(PyObject *lazy_import);
