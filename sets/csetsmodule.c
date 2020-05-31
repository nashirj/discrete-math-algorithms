#include <Python.h>

typedef unsigned int uint;
typedef unsigned long int ulong;

static PyObject* generate_power_set(PyObject* self, PyObject* args) {
    PyObject* listObj;
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &listObj))
        return NULL;

    uint len = PyList_Size(listObj);
    if (len > 27)
        return NULL;

    uint* set = malloc(len * sizeof(uint));
    PyObject* tmp;
    for (uint i = 0; i < len; i++) {
        tmp = PyList_GetItem(listObj, i);
        set[i] = PyLong_AsUnsignedLong(tmp);
    }

    double pset_size = pow(2, len);
    PyObject* pset = PyList_New(pset_size);

    for (uint i = 0; i < pset_size; i++) {
        uint subset_size = 0;
        uint n = i;
        // This while loop looks like a an O(n) operation, but since n is an 8 bit type, it's really constant time.
        // I've unrolled the loop since I'm not sure how smart the optimizer is
        subset_size += n & (uint) 1;
        n >>= (uint) 1;
        subset_size += n & (uint) 1;
        n >>= (uint) 1;
        subset_size += n & (uint) 1;
        n >>= (uint) 1;
        subset_size += n & (uint) 1;
        n >>= (uint) 1;
        subset_size += n & (uint) 1;
        n >>= (uint) 1;
        subset_size += n & (uint) 1;
        n >>= (uint) 1;
        subset_size += n & (uint) 1;
        n >>= (uint) 1;
        subset_size += n & (uint) 1;


        PyObject* subset = PyList_New(subset_size);
        int subset_index = 0;
        for (uint j = 0; j < len; j++) {
            if ((i & ((uint) 1 << j)) > 0) {
                PyList_SetItem(subset, subset_index, PyLong_FromUnsignedLong(set[j]));
                subset_index++;
            }
        }

        PyList_SetItem(pset, i, subset);
    }

    free(set);
    return pset;
}

static PyMethodDef CSetsMethods[] = {
        {"generate_pset", generate_power_set, METH_VARARGS, "Generate a power set from the given elements."},
        {NULL, NULL, 0, NULL}
};

static struct PyModuleDef csetsmodule = {
        PyModuleDef_HEAD_INIT,
        "csets",
        "Python C module for generating sets pertinent to discrete math",
        -1,
        CSetsMethods
};

PyMODINIT_FUNC PyInit_csets(void) {
    return PyModule_Create(&csetsmodule);
}