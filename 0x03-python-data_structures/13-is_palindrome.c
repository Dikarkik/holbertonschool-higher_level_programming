#include "lists.h"

/**
 * compare_head_tail - recursive function that find the end of
 * a single linked list and then compares head/tail
 * @curr_tail: pointer towards tail
 * @head: permanent reference to head
 * Return: a pointer towards head or NULL if head/tail are diferent
 */
listint_t *compare_head_tail(listint_t *curr_tail, listint_t *head)
{
	listint_t *curr_head;

	if (curr_tail == NULL)
		return (head);

	curr_head = compare_head_tail(curr_tail->next, head);

	if (curr_head == NULL)
		return (NULL);

	if (curr_head->n == curr_tail->n)
		if (curr_head->next == NULL)
			return (head); /* end of comparations */
		else
			return (curr_head->next);
	else
		return (NULL);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *result;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	result = compare_head_tail(*head, *head);

	if (result)
		return (1);

	return (0);
}
