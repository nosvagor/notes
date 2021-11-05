//Header comments with my name and purpose of the info in this file.   
#include <iostream>
using namespace std;

bool again(); //This function is provided for you

//Let's begin with linear linked lists by having a list of integer data
struct node
{
       int data;
       node * next;
};

/*
The public section can be used by any object. 
Usually member functions are public while data
members are private. 

Member functions describe what a class does! 
Data describes what a class is.  */
class list
{
    public:
    // YOU will be implementing these for Lab #7 
        list();                //Constructor - initializes data members
        void display_all();    //Display all data within the LLL
        int count_first();     //Count how many times the first itemp appears
        void display_last();
        bool find_last();      //Find if the last node's data duplicated?


    //***************************************************************
    // THESE FUNCTIONS Have already been implemented for you 
        ~list();              //Destructor - deallocates all dynamic memory
        void build();         //Inserts data into the LLL from the user
    private:
        node * head;          //The head of a linear linked list
        
};
