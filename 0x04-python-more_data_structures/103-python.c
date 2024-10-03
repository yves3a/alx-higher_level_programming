#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the PyObject representing the list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	printf("  first %ld bytes:", (size > 10 ? 10 : size));
	for (i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf(" %.2x", (unsigned char)bytes[i]);
	}
	printf("\n");
}

