#include "lists.h"

/**
 * list_len - returns the number of elements in a linked list_t list.
 * @h: list_t list.
 * Return: the number of elements in a linked list_t list.
 */
int list_len(const listint_t *h)
{
	int index = 0;

	while (h != NULL)
	{
		index++;
		h = h->next;
	}

	return (index);
}

/**
 * reverse - reverse
 * @head: head
 * Return: void
 */
void reverse(listint_t **head)
{
	listint_t *next = NULL, *current = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = current;
		current = *head;
		*head = next;
	}
	*head = current;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node = NULL;
	int len = 0, index = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	node = *head;
	len = list_len(*head);
	if (len % 2 == 0)
	{
		len = len / 2;
		len -= 1;
	}
	else
		len = len / 2;
	while (index <= len)
	{
		node = node->next;
		index++;
	}
	reverse(&node);
	while (node)
	{
		if (node->n != (*head)->n)
		return (0);
		node = node->next;
		*head = (*head)->next;
	}
	return (1);
}
