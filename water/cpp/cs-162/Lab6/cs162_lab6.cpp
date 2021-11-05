//Put your header comments here with your name, class
//and purpose of the program

#include "cs162_course.h"





int main()
{

    course me;
    //Step #4 - Create an object of the class here:

    me.read_name();
    me.display_name();


    char a_first_name[SIZE];
    char a_last_name[SIZE];

    me.read_course();
    me.display();

    cout << "\nComparing name...\n\nFirst name: ";
    cin.get(a_first_name, SIZE, '\n');
    cin.ignore(100, '\n');

    cout << "Last name: ";
    cin.get(a_last_name, SIZE, '\n');
    cin.ignore(100, '\n');

    a_first_name[0] = toupper(a_first_name[0]);
    a_last_name[0] = toupper(a_last_name[0]);

    if (me.is_match(a_first_name, a_last_name)) {
      cout << "\nThis student is enrolled in the course!" << endl;
    } else {
      cout << "\nNo match found" << endl;
    }

    //Steps #5-10 - Call the member functions here:



    return 0;
}
