#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *head_2;
	listint_t *prev_2 = NULL;
	listint_t *current_again;
	listint_t *head_2_again;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	while (current)
	{
		head_2 = malloc(sizeof(listint_t));
		head_2->n = current->n;
		head_2->next = prev_2;
		prev_2 = head_2;
		current = current->next;
	}

	current_again = *head;
	head_2_again = head_2;
	while (current_again)
	{
		if (current_again->n != head_2_again->n)
		{
			free(head_2);
			return (0);
		}
		current_again = current_again->next;
		head_2_again = head_2_again->next;
	}
	free(head_2);
	return (1);
}
