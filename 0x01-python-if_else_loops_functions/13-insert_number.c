#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * createNode - Creates a new node with the given number
 * @number: The number to be stored in the new node
 *
 * Return: Address of the new node, or NULL if memory allocation failed
 */
listint_t *createNode(int number)
{
    listint_t *newNode = malloc(sizeof(listint_t));
    if (newNode != NULL)
    {
        newNode->n = number;
        newNode->next = NULL;
    }
    return newNode;
}

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to the head of the linked list
 * @number: The number to be inserted
 *
 * Return: Address of the new node, or NULL if memory allocation failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *previous;
    listint_t *newNode = createNode(number);
    if (newNode == NULL)
        return NULL;

    current = *head;
    previous = NULL;

    /* Traverse the list to find the appropriate position to insert the new node */
    while (current != NULL && current->n < number)
    {
        previous = current;
        current = current->next;
    }

    if (previous == NULL)
    {
        /* The new node should be the new head of the list */
        newNode->next = *head;
        *head = newNode;
    }
    else
    {
        /* Insert the new node between previous and current */
        previous->next = newNode;
        newNode->next = current;
    }

    return newNode;
}
