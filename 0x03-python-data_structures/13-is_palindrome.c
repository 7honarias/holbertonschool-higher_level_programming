#include "lists.h"

/**
 * is_palindrome - function valide palindrome of list
 * @head: head of list
 * Return: 1 if is palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *last = NULL;
	int x;
	int count = 0;

	if (head && *head)
	{
		while (temp)
		{
			x = temp->n;
			add_nodeint_end(&last, x);
			count++;
			temp = temp->next;
		}
		temp = *head;
		while (temp)
		{
			if (temp->n != last->n)
				return (0);
			temp = temp->next;
			last = last->next;
		}
	}
	free_listint(last);
	return (1);
}
