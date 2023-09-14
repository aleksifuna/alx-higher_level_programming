#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_list - prints some basic info of a list
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	int i;
	PyListObject *list;

	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < list->ob_base.ob_size; i++)
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
}
/**
 * print_python_bytes - prints some basic info of a string byte
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *str;
	int size;

	str = (PyBytesObject *)p;
	size = str->ob_base.ob_size;
	printf("[.] bytes object info\n");
	printf("  size: %s\n",str->ob_base.ob_base.ob_type->tp_name);
	printf("  size: %d\n",size);
	printf("  trying string: %s\n", str->ob_sval);
}
