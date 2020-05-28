#include <Python.h>

static PyObject* generate_power_set(PyObject* self, PyObject* args) {
    PyObject* listObj;
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &listObj))
        return NULL;

    uint len = PyList_Size(listObj);
    if (len > 25)
        return NULL;

    ulong* set = malloc(len * sizeof(ulong));
    PyObject* item;
    for (uint i = 0; i < len; i++) {
        item = PyList_GetItem(listObj, i);
        set[i] = PyLong_AsUnsignedLong(item);
    }

    double pset_size = pow(2, len);
    PyObject* pset = PyList_New(pset_size);

    for (uint i = 0; i < pset_size; i++) {
        uint subset_size = 0;
        uint n = i;
        // This while loop looks like a an O(n) operation, but since n is an 8 bit type, it's really constant time.
        while (n) {
            subset_size += n & (uint) 1;
            n >>= (uint) 1;
        }

        PyObject* subset = PyList_New(subset_size);
        PyObject* current_item = NULL;
        int subset_index = 0;
        for (uint j = 0; j < subset_size; j++) {
            if ((i & ((uint) 1 << j)) > 0) {
                current_item = PyLong_FromUnsignedLong(set[j]);
                PyList_SetItem(subset, subset_index, current_item);
                subset_index++;
            }
        }

        PyList_SetItem(pset, i, subset);
    }

    free(set);
    return pset;
}

static PyMethodDef SetsMethods[] = {
        {"generate_pset", generate_power_set, METH_VARARGS, "Generate a power set from the given elements."},
        {NULL, NULL, 0, NULL}
};

static struct PyModuleDef setsmodule = {
        PyModuleDef_HEAD_INIT,
        "sets",
        "Python module for generating sets pertinent to discrete math",
        -1,
        SetsMethods
};

PyMODINIT_FUNC PyInit_sets(void) {
    return PyModule_Create(&setsmodule);
}