#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head of a listint_t list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (!list)
		return (0);

	if (!list->next)
		return (0);

	current = list->next;

	while (current)
	{
		if (current == list)
			return (1);

		current = current->next;
	}

	return (0);
}
