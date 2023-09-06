#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node into a sorted singly linked list
 * @head: pointer to head node
 * @number: number to be inserted
 *
 * Return: address of new node of NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	current = *head;
	if (number < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current != NULL)
	{
		if (current->next != NULL)
		{
			if (number >= current->n && number < current->next->n)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			else
				current = current->next;
		}
		else
		{
			new->next = NULL;
			current->next = new;
			return (new);
		}
	}
	return (NULL);
}
