#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to the head of the list
 * @number: number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current;

    /* allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;

    /* initialize the new node */
    new_node->n = number;
    new_node->next = NULL;

    /* if the list is empty, insert the new node at the head */
    if (*head == NULL) {
        *head = new_node;
        return new_node;
    }

    /* traverse the list to find the correct position to insert the new node */
    current = *head;
    while (current->next != NULL && current->next->n < number)
        current = current->next;

    /* insert the new node into the list */
    new_node->next = current->next;
    current->next = new_node;

    return new_node;
}