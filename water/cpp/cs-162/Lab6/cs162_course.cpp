//Include your name, course, and information about the code
//implemented in this file.

#include "cs162_course.h"

//Implement the body of these functions for Lab #6

//Constructor - initialize all data members to their zero equivalent value
course::course()
{
  crn[0] = '\0';
  description[0] = '\0';
  section[0] = '\0';
}


//Read in the CRN, Course Description and Section
//Store these into the private data members of the class
void course::read_course()
{
  cout << "\nCRN: ";
  cin.get(crn, SIZE, '\n');
  cin.ignore(100, '\n');

  cout << "Course description: ";
  cin.get(description, SIZE, '\n');
  cin.ignore(100, '\n');

  cout << "Section: ";
  cin.get(section, SIZE, '\n');
  cin.ignore(100, '\n');
}


//Display the name and course information
void course::display()
{
  cout << "\nHello, " << first_name << " " << last_name << endl
       << "Your course: \n";

  cout << "CRN: " << crn << " (" << section << ")"
       << " --- " << description
       << endl;
}

//Take the argument and compare it to the student's name
//If it is the same, return a true - otherwise return false
bool course::is_match(char a_first_name[], char a_last_name[])
{
  bool res = false;

  (!strcmp(a_first_name, first_name)) ? res = true : res = false;
  (!strcmp(a_last_name, last_name)) ? res = true : res = false;

  return res;
}


//Reset the course information for a student if they
//want to drop, given the CRN. Only drop the course if the CRN
//matches. Return true if the operation was successful and false
//if the CRN doesn't match
bool course::drop(int CRN)
{
      //Implement this function

  return false;
}


