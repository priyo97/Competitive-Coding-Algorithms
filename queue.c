/*
Program implementing a Queue using LinkedList

A layer of abstraction is implemented:
 - queue_t - has to be declared and initialized and it contains all the necessary information about the queue
 - enqueue - Insert a Node at the End of the queue
 - dequeue - Delete a Node at the Beg of the queue

 Note: Modifiy the main function according the requirements. Currently manually inserting and deleting for testing purposes 
*/


#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int data;
    struct Node *next;
    
} Node;

typedef struct queue
{
    Node *head;
    Node *tail;
    int length;
    
} queue_t;

Node* create_node(int data)
{
    Node *new_node = (Node *) malloc(sizeof(Node));

    if(new_node != NULL)
    {
        new_node -> data = data;
        new_node -> next = NULL;
    }

    return new_node;
}

void enqueue(queue_t *pq, int data)
{
    Node *new_node = create_node(data);
   
    if(new_node != NULL)
    {
        if(pq -> length == 0)
        {
            pq -> head = new_node;
            pq -> tail = new_node;
        }
        else
        {
            pq -> tail -> next = new_node;
            pq -> tail = new_node;
        }

        pq -> length += 1;
    }
}


Node* dequeue(queue_t *pq)
{
    Node *tmp;

    if(pq -> length == 0)
    {
        printf("Queue is Empty\n");
        return NULL;
    }

    tmp = pq -> head;
    pq -> head = pq -> head -> next;
    pq -> length -= 1;

    if(pq -> length == 0)
    {
        pq -> head = pq -> tail = NULL;
    }

    tmp -> next = NULL;
    return tmp; 
}

void display_queue(queue_t *pq)
{
    Node *tmp = pq -> head;
    printf("Head");
    
    while(tmp != NULL)
    {
        printf(" -> %d", tmp -> data);
        tmp = tmp -> next;
    }
    
    printf(" -> NULL\n");
}

void print_node(Node *ptr)
{
    printf("-------------------\n");
    printf("Contents of Node:\n");
    printf("node -> data: %d\n", ptr != NULL ? ptr -> data:-1);
    printf("node -> next: %p\n", ptr != NULL ? ptr -> next:NULL);
    printf("-------------------\n");
}

int main()
{
    queue_t pq = {NULL, NULL, 0};
    Node *tmp;

    // Enqueue operations
    enqueue(&pq, 5);
    enqueue(&pq, 1);
    enqueue(&pq, 4);
    enqueue(&pq, 3);
    enqueue(&pq, 6);
    enqueue(&pq, 2);

    display_queue(&pq);

    // Dequeue operations

    tmp = dequeue(&pq);
    print_node(tmp);
    tmp = dequeue(&pq); 
    tmp = dequeue(&pq);
    tmp = dequeue(&pq);
    tmp = dequeue(&pq);
    tmp = dequeue(&pq);
    print_node(tmp);
    tmp = dequeue(&pq);
    print_node(tmp);
}
