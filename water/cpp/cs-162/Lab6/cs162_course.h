//Put your header comments here with your name, class
//and purpose of the class

#include <iostream>
#include <cstring>
#include <cctype>
using namespace std;


/* Header files should include the following information:
   1. #includes
   2. structures
   3. prototypes
   4. class interfaces
   5. constants

   Never implement the body of funcctions in a .h file */

//Place your constants here:
const int SIZE {21};

//Here is the class we will be working with to represent
//a course that a student is taking. 
class course
{
    public:   //you will be implementing these functions:
       course();           //constructor
       void read_course(); //read in the course they are taking
       void display();     //display the course enrolled in
       bool is_match(char a_first_name[], char a_last_name[]); 
       bool drop(int CRN); //remove the course information if matches CRN


       //************************************************
       //These functions have already been written for you!
       void read_name();      //read in the user's name
       void display_name();   //display the name

       //This function copies the argument's first and last names into
       //the data member and may be useful for the challenge question
       void copy_name(char from_first[], char from_last[]); 

    private:
       char first_name[SIZE]; 
       char last_name[SIZE];
       //Place the rest of the data members here:




};

