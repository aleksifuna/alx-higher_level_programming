#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly list is a palindrome
 * @head: pointer to head node
 *
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	int i;
	int node;
	int list[3000];
	listint_t *current;

	current = *head;
	if (current == NULL || current->next == NULL)
		return (1);
	i = 0;
	while (current != NULL)
	{
		list[i] = current->n;
		i++;
		current = current->next;
	}
	node = i;
	for (i = 0; i < node / 2; i++)
	{
		if (list[i] != list[node - 1 - i])
			return (0);
	}
	return (1);
}
