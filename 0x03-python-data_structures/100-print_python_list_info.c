#include <Python.h>

/**
 * print_python_list_info - Prints Python lists
 * Description: prints some basic info about Python lists
 * @p: A PyObject list
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int al, s, i;
	PyObject *obj;

	s = Py_SIZE(p);
	al = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", al);
	i = 0;
	while (i < s)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		i++;
	}
}
