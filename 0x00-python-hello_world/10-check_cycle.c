#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdlib.h>
/**
 * check_cycle - verify a cycle in a list
 * Description: verify if it s a cycle in a list
 * @list: pointer to head of list
 * Return: address of the node insert
 */
int check_cycle(listint_t *list)
{
	listint_t *t = list;
	int i = 0;

	if (list == NULL)
		return (i);
	while (t != NULL)
	{
		if (t->next != NULL && t->next != list)
			t = t->next;
		else
			break;
	}
	if (t->next != NULL)
		i = 1;
	return (i);
}
