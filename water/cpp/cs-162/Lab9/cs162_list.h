//list.h
#include <iostream>
#include <cctype>
#include <cstdlib>


//Notice with this lab we are practicing with recursion
//The concept of a class is not being used
 
//The data structure is still a linear linked list
//However, main now manages the head pointer, since we are not
//using a class
struct node
{
    int data;
    node * next;
};

/* *****************YOUR TURN! ******************************** */
/* WRITE THESE FUNCTIONS...either recursively or iteratively */

bool find(node * head, int match);
int remove_all(node * & head);
int remove_all_2nd(node * & head);
int display_every_other(node * head);

//**********************************************
// These functions are already written and can be called to test out your code
void build(node * & head);      //supplied
void display_all(node * head);  //supplied
void destroy(node * &head);     //supplied


