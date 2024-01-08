#include "lists.h"

/**
  * reverse - Reverses
  * @head: the head
  * Return: The new head
  */

listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
  * is_palindrome - Checks for palindrome
  * @head: The linked list
  * Return: 1 if a palindrome, otherwise 0
  */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second_half, *first_half;

	slow = *head;
	fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = reverse(slow);
	first_half = *head;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return (0);

		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}
