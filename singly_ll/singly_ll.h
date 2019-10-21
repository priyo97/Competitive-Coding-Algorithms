#ifndef SINGLY_LL
#define SINGLY_LL

#define MAIN_MENU 1
#define SUB_MENU  2

enum Bool
{
    False,
    True
};

enum Operation
{
    INSERT=1,
    DELETE,
    DISPLAY,
    EXIT
};

enum Choice
{
    AT_BEG=1,
    AT_END,
    AT_POS
};

typedef struct Node
{
    int data;
    struct Node *next;

} Node;

typedef struct ll_details
{
    Node *head;
    int length;
} ll_details;

void print_banner();
void print_menu();
void operate_ll(ll_details *l);
void print_ll(Node *head);
int  get_input();
int get_pos(int cur_len, enum Operation opt);
void operate(enum Operation opt, enum Choice c, ll_details *l);
Node* create_node(int data);
void free_linked_list(ll_details *l);


#endif
