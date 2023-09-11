#include "lists.h"
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
	int first_half;
	int second_half;
	listint_t *current;

	first_half = second_half = node = i = 0;
	current = *head;
	if (current == NULL && current-next == NULL)
		return (1);
	while (current != NULL)
	{
		node++;
		current = current->next;
	}
	current = *head;
	while (current != NULL)
	{
		if (i < node / 2)
			first_half += current->n;
		else if (node % 2 != 0 && i == node / 2)
			first_half += 0;
		else
			second_half += current->n;
		i++;
		current = current->next;
	}
	if (first_half == second_half)
		return (1);
	return (0);
}
