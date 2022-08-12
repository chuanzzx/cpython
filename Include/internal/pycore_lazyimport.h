#ifndef Py_INTERNAL_LAZYIMPORTOBJECT_H
#define Py_INTERNAL_LAZYIMPORTOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

#ifndef Py_BUILD_CORE
#  error "this header requires Py_BUILD_CORE define"
#endif


PyAPI_DATA(PyTypeObject) PyLazyImport_Type;

#define PyLazyImport_CheckExact(op) Py_IS_TYPE((op), &PyLazyImport_Type)


typedef struct {
    PyObject_HEAD
    PyObject *lz_lazy_import;
    PyObject *lz_name;
    PyObject *lz_globals;
    PyObject *lz_locals;
    PyObject *lz_fromlist;
    PyObject *lz_level;
    PyObject *lz_resolved;
    PyObject *lz_resolving;
} PyLazyImportObject;


PyAPI_FUNC(PyObject *) PyLazyImport_GetName(PyObject *lazy_import);
PyAPI_FUNC(PyObject *) PyLazyImport_NewModule(PyObject *name, PyObject *globals, PyObject *locals, PyObject *fromlist, PyObject *level);
PyAPI_FUNC(PyObject *) PyLazyImport_NewObject(PyObject *from, PyObject *name);


#ifdef __cplusplus
}
#endif
#endif /* !Py_INTERNAL_LAZYIMPORTOBJECT_H */
