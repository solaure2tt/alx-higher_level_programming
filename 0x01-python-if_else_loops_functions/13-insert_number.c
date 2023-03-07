#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - insert a node in a listint_t list
 * Description: insert a node in a right place in a list
 * @head: pointer to head of list
 * @number: number to insert
 * Return: address of the node insert
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *res;
	listint_t *h, *tmp;

	tmp = *head;
	res = malloc(sizeof(listint_t));
        if (res == NULL)
                return (NULL);
        res->n = number;
	if (tmp == NULL)
	{
		res->next = NULL;
		return (res);
	}
	if (tmp->n > number)
	{
		res->next = tmp;
		return (res);
	}
	while (tmp != NULL && tmp->n <= number)
	{
		h = tmp;
		tmp = tmp->next;
	}
	h->next = res;
	if (tmp != NULL)
		res->next = tmp;
	else
		res->next = NULL;
	return (res);
}
