//list.h
#include <iostream>
#include <cctype>
#include <cstdlib>


//The data structure is a linear linked list of integers
struct node
{
    int data;
    node * next;
};


//Implement these functions either iteratively or recursively
int display_first_and_last(node * head);
bool insert_before_last(node * & head, int to_add);
int remove_first_two(node * & head);

//Challenge
void copy_all(node * & destination_head, node * source_head);


//****************************************************
/* These functions are already written and 
   can be called to test out your code */
void build(node * & head);      //supplied
void display_all(node * head);  //supplied
void destroy(node * &head);     //supplied


