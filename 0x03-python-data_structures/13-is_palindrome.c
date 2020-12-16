#include "lists.h"

/**
 * is_palindrome - function valide palindrome of list
 * @head: head of list
 * Return: 1 if is palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *temp_last = NULL;
	listint_t *last = NULL;
	int x;

	if (head && *head)
	{
		while (temp)
		{
			x = temp->n;
			add_nodeint(&last, x);
			temp = temp->next;
		}
		temp = *head;
		temp_last = last;
		while (temp)
		{
			if (temp->n != temp_last->n)
				return (0);
			temp = temp->next;
			temp_last = temp_last->next;
		}
	}
	free_listint(last);
	return (1);
}

/**
 * add_nodeint - add node to list
 * @head: head of list
 * @n: number to add
 * Return: pointer new head
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	(*head) = new;

	return (new);
}
