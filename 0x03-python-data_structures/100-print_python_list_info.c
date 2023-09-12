#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints some basic information for a python list
 * @p: pointer to a python object
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *list;
	PyObject *x;
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < list->ob_base.ob_size; i++)
	{
		x = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, (Py_TYPE(x))->tp_name);
	}
}
