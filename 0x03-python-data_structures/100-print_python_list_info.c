#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic information about a Python list object
 * @p: Pointer to the Python list object
 *
 * Description: This function prints the size, allocated memory, and the type of
 * each element in the Python list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
