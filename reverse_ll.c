#include<stdio.h>
#include<stdlib.h>

typedef struct Node
{
    int data;
    struct Node *next;

} Node;

Node* create_node(int data);
void insert_node(Node **head_ref, int data);
void reverse_linked_list(Node **head_ref);
void display_list(Node *head);
void free_linked_list(Node **head_ref);

int main()
{
    Node *head = NULL;

    insert_node(&head, 2);
    insert_node(&head, 3);
    insert_node(&head, 4);
    insert_node(&head, 5);
    insert_node(&head, 6);

    printf("Before, reversing...\n");
    display_list(head);

    reverse_linked_list(&head);

    printf("After, reversing...\n");
    display_list(head);

    free_linked_list(&head);
}


Node* create_node(int data)
{
    Node *ptr = (Node*)malloc(sizeof(Node));
    ptr -> data = data;
    ptr -> next = NULL;
    return ptr;
}

void insert_node(Node **head_ref, int data)
{ 
    Node *new_node = create_node(data);
   
    new_node -> next = *head_ref;

    *head_ref = new_node; 
}

void reverse_linked_list(Node **head_ref)
{
    Node *prev, *current, *next;
    prev = current = next = NULL;

    current = *head_ref;

    while(current != NULL)
    {
        next = current -> next; 
        current -> next = prev;
        prev = current;
        current = next;
    }

    *head_ref = prev;
}

void display_list(Node *head)
{
    Node *tmp;

    printf("HEAD");

    if(head != NULL)
    {
        tmp = head;
        while(tmp != NULL)
        {
            printf(" -> %d", tmp -> data);
            tmp = tmp -> next;
        }
    }

    printf(" -> NULL\n");
}

void free_linked_list(Node **head_ref)
{
    Node *tmp;
    while(*head_ref != NULL)
    {
        tmp = *head_ref;
        *head_ref = (*head_ref) -> next;
        free(tmp);
    }
}
