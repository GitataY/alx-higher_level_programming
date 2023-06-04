#include <Python.h>

void print_python_string(PyObject *p) {
    PyUnicodeObject *str_obj = (PyUnicodeObject *)p;
    Py_ssize_t length = PyUnicode_GET_LENGTH(str_obj);
    Py_UNICODE *value = PyUnicode_AS_UNICODE(str_obj);

    printf("[.] string object info\n");
    printf("  type: compact %s\n", PyUnicode_IS_ASCII(str_obj) ? "ascii" : "unicode object");
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", value);
}
