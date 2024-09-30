#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listint - Reverses a listint_t linked list.
 * @head: Pointer to a pointer pointing to the head node.
 *
 * Return: Pointer to the new head node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer pointing to the head node.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half = NULL;
	listint_t *prev_slow = *head;
	listint_t *mid_node = NULL;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			mid_node = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_slow->next = NULL;
		reverse_listint(&second_half);
		is_palindrome = compare_lists(*head, second_half);

		if (mid_node != NULL)
		{
			prev_slow->next = mid_node;
			mid_node->next = second_half;
		}
		else
			prev_slow->next = second_half;
	}

	return (is_palindrome);
}

/**
 * compare_lists - Compares two linked lists for equality.
 * @head1: Pointer to the head node of the first list.
 * @head2: Pointer to the head node of the second list.
 *
 * Return: 1 if the lists are equal, 0 otherwise.
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}

