#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * reverselist -  add a node at the head of a list
 * Description: add a node at the head of a list
 * @h: list
 * Return: a list
 */
listint_t *reverselist(listint_t *h)
{
	listint_t *new, *res, *tmp = h;

	res = NULL;
	while (tmp != NULL)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = tmp->n;
		new->next = res;
		res = new;
		tmp = tmp->next;
	}
	return (res);
}


/**
 * is_palindrome - test id a list s a palindrome
 * Description: verify if a list is a palindrome
 * @head: list
 * Return: 1 if true or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *t;
	int res = 0;

	if (*head == NULL)
		return (1);
	tmp = *head;
	t = reverselist(tmp);
	while (tmp != NULL && tmp->n == t->n)
	{

		tmp = tmp->next;
		t = t->next;
	}
	if (tmp == NULL)
		res = 1;
	free_listint(t);
	return (res);
}
