#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if there is a cycle within the lists
 * @list: linked lists to check from.
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_p, *fast_p;

	/*when a list is empty*/
	if (list == NULL)
		return (0);

	slow_p = fast_p = list;
	/*it iterates through the lists and see if there is infinite connection*/

	while (fast_p != NULL && fast_p->next != NULL)
	{
		fast_p = fast_p->next->next;
		slow_p = slow_p->next;

		if (slow_p == fast_p)
			return (1);/*there is a cycle within the list*/
	}
	return (0);/*there is no cycle*/
}
