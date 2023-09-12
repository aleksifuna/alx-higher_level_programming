#include <Python.h>
void print_python_list_info(PyObject *p);
/**
 * print_python_list_info - prints some basic information for a python list
 * @p: pointer to a python object
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *list;
	PyObject *x;
	int list_size;

	list_size = PyList_Size(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %lu\n", list->allocated);
	for (i = 0; i < list_size; i++)
	{
		x = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, (Py_TYPE(x))->tp_name);
	}
}
