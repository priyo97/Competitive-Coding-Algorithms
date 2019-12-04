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

typedef struct Packet
{
    char data;
    int id;
} Packet;

typedef struct Node
{
    Packet p;
    struct Node *prev;
    struct Node *next;
    
} Node;

typedef struct queue
{
    Node *head;
    Node *tail;
    int length;
    
} queue_t;

Node* create_node(Packet data)
{
    Node *new_node = (Node *) malloc(sizeof(Node));

    if(new_node != NULL)
    {
        new_node -> p    = data;
        new_node -> prev = NULL;
        new_node -> next = NULL;
    }

    return new_node;
}

void enqueue_sorted(queue_t *pq, Packet data)
{
    Node *tmp;
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
            tmp = pq -> head;

            while( tmp != NULL && ((tmp -> p).id < (new_node -> p).id) )
            {
                tmp = tmp -> next;
            }

            if(tmp == NULL)
            {
                pq -> tail -> next = new_node;
                new_node -> prev   = pq -> tail;
                pq -> tail         = new_node;
            }
            else if(tmp == pq -> head)
            {
                pq -> head -> prev = new_node;
                new_node -> next   = pq -> head;
                pq -> head         = new_node;
            }
            else
            {
                new_node -> prev    = tmp -> prev; 
                new_node -> next    = tmp; 
                tmp -> prev -> next = new_node;
                tmp -> prev         = new_node;
            }
        }

        pq -> length += 1;
    }
}


void display_queue(queue_t *pq)
{
    Node *tmp = pq -> head;
    printf("Head");
    
    while(tmp != NULL)
    {
        printf(" -> |%c, %d|", (tmp -> p).data, (tmp -> p).id);
        tmp = tmp -> next;
    }
    
    printf(" -> NULL\n");
}

int main()
{
    queue_t pq = {NULL, NULL, 0};
    Node *tmp;

    Packet p[6] = {{'B', 2}, {'F', 6}, {'D', 4}, {'E', 5}, {'C', 3}, {'A', 1}};

    // Enqueue operations
    enqueue_sorted(&pq, p[0]);
    enqueue_sorted(&pq, p[1]);
    enqueue_sorted(&pq, p[2]);
    enqueue_sorted(&pq, p[3]);
    enqueue_sorted(&pq, p[4]);
    enqueue_sorted(&pq, p[5]);

    display_queue(&pq);

}
