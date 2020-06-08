#include <Python.h>

typedef unsigned int uint;
typedef unsigned long int ulong;

static PyObject* _gen_pset_from_c_arr(uint* set, uint size) {
    double pset_size = pow(2, size);
    PyObject* pset = PyList_New(pset_size);

    for (uint i = 0; i < pset_size; i++) {
        uint subset_size = 0;
        uint n = i;
        // Unrolled the loop since I'm not sure how smart the optimizer is
        while (n) {
            subset_size += n & (uint) 1;
            n >>= (uint) 1;
        }


        PyObject* subset = PyList_New(subset_size);
        int subset_index = 0;
        for (uint j = 0; j < size; j++) {
            if ((i & ((uint) 1 << j)) > 0) {
                PyList_SetItem(subset, subset_index, PyLong_FromUnsignedLong(set[j]));
                subset_index++;
            }
        }

        PyList_SetItem(pset, i, subset);
    }

    return pset;
}

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
        if (!PyNumber_Check(tmp))
            return NULL;

        set[i] = PyLong_AsUnsignedLong(tmp);
    }

    PyObject* pset = _gen_pset_from_c_arr(set, len);
    free(set);
    return pset;
}

static PyObject* _gen_cset_from_c_arr(uint* set, uint size) {
    PyObject* cset = PyList_New(pow(size, 2));
    uint cset_index = 0;

    for (uint i = 0; i < size; i++) {
        for (uint j = 0; j < size; j++) {
            PyObject* pair = PyTuple_New(2);
            PyTuple_SetItem(pair, 0, PyLong_FromLong(set[i]));
            PyTuple_SetItem(pair, 1, PyLong_FromLong(set[j]));
            PyList_SetItem(cset, cset_index, pair);

            cset_index++;
        }
    }

    return cset;
}

static PyObject* generate_cartesian_product(PyObject* self, PyObject* args) {
    PyObject* listObj;
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &listObj))
        return NULL;

    uint len = PyList_Size(listObj);
    if (len > 24000)
        return NULL;

    uint* set = malloc(len * sizeof(uint));
    PyObject* tmp;
    for (uint i = 0; i < len; i++) {
        tmp = PyList_GetItem(listObj, i);
        if (!PyNumber_Check(tmp))
            return NULL;

        set[i] = PyLong_AsUnsignedLong(tmp);
    }

    PyObject* cset = _gen_cset_from_c_arr(set, len);

    free(set);
    return cset;
}

PyObject* generate_cartesian_product_n_elements(PyObject* self, PyObject* args) {
    uint n;
    if (!PyArg_ParseTuple(args, "I", &n))
        return NULL;

    uint* set = malloc(n * sizeof(uint));
    for (uint i = 0; i < n; i++) {
        set[i] = i + 1;
    }
    PyObject* cset = _gen_cset_from_c_arr(set, n);

    free(set);
    return cset;
}

static PyMethodDef CSetsMethods[] = {
        {"generate_pset", generate_power_set, METH_VARARGS, "Generate a power set from the given elements."},
        {"generate_cartesian_product", generate_cartesian_product, METH_VARARGS,
            "Generate the cartesian product of a given set"},
        {"generate_cartesian_product_n_elements", generate_cartesian_product_n_elements, METH_VARARGS,
            "Generate the cartesian product of the sequence 1..n"},
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