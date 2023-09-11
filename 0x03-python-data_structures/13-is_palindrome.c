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
	int i, j;
	int node;
	int first;
	int second;
	listint_t *current, *temp;

	node = i = 0;
	current = *head;
	if (current == NULL || current->next == NULL)
		return (1);
	while (current != NULL)
	{
		node++;
		current = current->next;
	}
	current = *head;
	while (i < node / 2)
	{
		first = current->n;
		j = i;
		temp = current;
		while (j != node - 1 - i)
		{
			temp = temp->next;
			j++;
		}
		second = temp->n;
		if (first != second)
			return (0);
		i++;
		current = current->next;
	}
	return (1);
}
