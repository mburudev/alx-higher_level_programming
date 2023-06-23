#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, typeName);
    }
}

void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_GET_SIZE(p);
    const char *data = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", data);

    if (size > 10)
        size = 10;

    printf("  first %ld bytes: ", size);
    for (Py_ssize_t i = 0; i < size; i++) {
        printf("%02x", data[i] & 0xff);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}
