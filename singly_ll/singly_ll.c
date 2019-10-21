#include <stdio.h>
#include <stdlib.h>
#include "singly_ll.h"

int main()
{
    struct ll_details l1 = {NULL, 0};
    print_banner();
    operate_ll(&l1);
}

Node* create_node(int data)
{
    Node *ptr = (Node*) malloc(sizeof(Node));
    ptr -> data = data;
    ptr -> next = NULL;

    return ptr;
}

void insert_node(int pos, ll_details *l)
{
    int counter, data;
    Node *tmp = NULL;
    Node **head_ref = &(l -> head);

    printf("Enter data: ");
    scanf("%d", &data);

    Node *new_node = create_node(data);

    if(pos == 1)
    {
        new_node -> next = *head_ref;
        *head_ref = new_node;
    }
    else
    {
        counter = 1;

        tmp = *head_ref; 

        while(counter < pos - 1)
        {
            tmp = tmp -> next;
            counter += 1;
        }

        new_node -> next = tmp -> next;
        tmp -> next = new_node;
    }

    l -> length += 1;
    
}

void delete_node(int pos, ll_details *l)
{
    int counter;
    Node *tmp, *free_node;
    Node **head_ref = &(l -> head);

    tmp = free_node = NULL;

    if(pos == 1)
    {
        free_node = *head_ref;
        *head_ref = (*head_ref) -> next;
    }
    else
    {
        counter = 1;

        tmp = *head_ref; 

        while(counter < pos - 1)
        {
            tmp = tmp -> next;
            counter += 1;
        }

        free_node = tmp -> next; 
        tmp -> next = free_node -> next;
    }

    free(free_node);

    l -> length -= 1;
}
void operate(enum Operation opt, enum Choice c, ll_details *l)
{
    int pos;
    
    if(opt == INSERT)
    {
        switch(c)
        {
            case AT_BEG:
                insert_node(1, l);
                break;
            case AT_END:
                insert_node((l -> length) + 1, l);
                break;
            case AT_POS:
                pos = get_pos(l -> length, opt);
                insert_node(pos, l);
                break;
        }
    }
    else
    { 
        if(l -> length > 0)
        {
            switch(c)
            {
                case AT_BEG:
                    delete_node(1, l);
                    break;
                case AT_END:
                    delete_node((l -> length), l);
                    break;
                case AT_POS:
                    pos = get_pos(l -> length, opt);
                    delete_node(pos, l);
                    break;
            }
        }
        else
        {
            printf("Error: Length is list is 0\n");
        }
    }
}

int get_pos(int cur_len, enum Operation opt)
{
    int n;

    while(True)
    {
        printf("Enter Pos: ");
        scanf("%d", &n);

        if(opt == DELETE && (n > cur_len || n < 1))
            printf("Error: Invalid Delete Pos | Length: %d\n", cur_len);
        else if(opt == INSERT && (n > cur_len + 1 || n < 1))
            printf("Error: Invalid Insert Pos | Length: %d\n", cur_len);
        else
            return n;
    }
    
}

int get_input()
{
    int n;
    while(True)
    {
        printf(">> ");
        scanf("%d", &n);

        if(n < 0 || n > 4)
            printf("Error: Invalid Entry\n");
        else
            return n;
    }
}

void operate_ll(ll_details *l)
{
    int opt1, opt2;

    while(True)
    {
        print_menu(MAIN_MENU);
        opt1 = get_input();
        
        switch(opt1)
        {
            case INSERT:
            case DELETE:
                print_menu(SUB_MENU);
                opt2 = get_input();

                if(opt2 == EXIT)
                {
                    free_linked_list(l);
                    exit(0);
                }

                operate(opt1, opt2, l);
                break;
            case DISPLAY:
                printf("DISPLAYING...");
                print_ll(l->head);
                break;
            case EXIT:
                free_linked_list(l);
                exit(0);
                break;
        }
    }
}


void print_banner()
{
    printf("WELCOME TO SINGLY LINKED LIST\n");
    printf("=============================\n\n");
}

void print_menu(int opt)
{
    if(opt == MAIN_MENU)
        printf("1. Insert\n2. Delete\n3. Display\n4. Exit\n");
    else
        printf("1. At Beg\n2. At End\n3. At Pos\n4. Exit\n");
}

void print_ll(Node *head)
{
    printf("\nHEAD");

    while(head != NULL)
    {
        printf(" -> %d", head -> data);
        head = head -> next;
    }
    
    printf(" -> NULL\n");
}

void free_linked_list(ll_details *l)
{
    Node *tmp, *free_node;

    tmp = l -> head;
    free_node = NULL;
    
    while(tmp!=NULL)
    {
        free_node = tmp;
        tmp = tmp -> next;
        free(free_node); 
    }
}
