#include "lists.h"

/**
 * get_nodeint_at_index - returns the nth node of a listint_t linked list.
 * @head: pointer to head.
 * @index: index of the node, starting at 0.
 * Return: the node in the position index.
 * if the node does not exist, return NULL.
 */
int get_int_at_index(listint_t *head, int index)
{
	int count = 0;

	while (head)
	{
		if (count == index)
			return (head->n);
		head = head->next;
		count++;
	}

	return (0);
}

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
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node = NULL;
	int i = 0, len = 0;

	if (*head == NULL)
		return (1);
	node = *head;
	len = list_len(*head);
	while (i  != len)
	{
		if (node->n != get_int_at_index(*head, len - 1))
			return (0);
		node = node->next;
		i++;
		len--;
	}
	return (1);
}
