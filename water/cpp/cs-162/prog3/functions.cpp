// ┌─┐┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// ├┤ │ │││││   │ ││ ││││└─┐
// └  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘
// cullyn --- cs162
// Purpose: implementation of core functions of the program, does not include
// class methods.

#include "main.h"

//=============================================================================

// menu displays menu options and waits until a valid entry is given, passing
// result as an int to a switch statement.
int menu() {
  int selection {0};    // used for cases, see menu greeting for mappings.

  menu_greeting();

  do {
    cout << "Please select a menu option: ";
    cin >> selection;
    cin.clear();
    cin.ignore(420, '\n');
  } while (selection < 1 || selection > 8);

  return selection;
}


// yes_no is a confirmation function that takes in a custom array
// of characters and returns a boolean (no=false, yes=true)
char yes_no(const char * str) {
  char response;

  do {
    cout << str << " [y/n]: ";
    cin >> response;
    tolower(response);
    cin.ignore(420, '\n');
    if (response == 'n') return 'n';
  } while (response != 'y');

  return 'y';
}



// sleep delays program for set period of time (milliseconds), useful for
// displaying warning messages.
void sleep(int ms) {
  this_thread::sleep_for(chrono::milliseconds(ms));
}



// return_to_menu provides a short delay before returning to menu selection;
// includes animated ellipses for UX experience to indicate program isn't frozen.
void return_to_menu() {
    cout << "\nReturning to menu" << flush;

    for (int i = 0; i < 4; ++i) {
      sleep(2000/4);
      cout << "."<< flush;
    }
    cout << endl;
}



// file_reset takes the original animal provided and overwrites any appended
// content to the main working file (animals.txt)
void file_reset() {
  if (yes_no("\nReset current animal list?") == 'y') {

    // local variables
    int N = 512;        // line size, large just in case
    ifstream in_file;   // in file (src/animals_original.txt)
    ofstream out_file;  // out file (src/animals.txt)

    char line[N];       // get line input

    in_file.open(ORIGINAL);

    if (in_file) {

      out_file.open(CURRENT);

      if (out_file) {

        in_file.get(line, N, '\n');
        in_file.ignore(100, '\n');

        while (in_file && !in_file.eof()) {

          out_file << line << endl;
          in_file.get(line, N*6, '\n');
          in_file.ignore(100, '\n');
        }
      }
      out_file.close();
    }
    in_file.close();
  }
}


// greeting displays basics instructions on program start and restart
void greeting() {
  cout
    << endl
    << "\t\t\t ╔═╗┌┐┌┬┌┬┐┌─┐┬    ╔═╗┌─┐┬─┐┌┬┐ \n"
    << "\t\t\t ╠═╣│││││││├─┤│    ╠╣ ├─┤├┬┘│││ \n"
    << "\t\t\t ╩ ╩┘└┘┴┴ ┴┴ ┴┴─┘  ╚  ┴ ┴┴└─┴ ┴ \n"
    << endl;

  cout
    << "Animals should be equal, free, and happy! All animals described in this program\n"
    << "have not been harmed and provide invaluable services to others that they love."
    << endl << endl;

  cout
    << "This program keep track of animals with that provide such services.\n"
    << "We do our best to make any animal at this farm feel happy and respected."
    << endl << endl;

  cout
    << "Users of this program are free to add new animals manually, or provide\n"
    << "a list of animals that wish to join the farm.\n\n"
    << "\t Max capacity: " << MAX << "\n"
    << "New members of our farm require a name, species, breed, service they \n"
    << "provide to be admitted; other additional information may be added if desired."
    << endl << endl;

  cout
    << "Users may also simply list the animals currently in the farm.\n"
    << "Menu options will be provided to navigate the functionality of this program."
    << endl;
}


// incoming_greeting displays instructions for loading an external file for
// animal registration.
void incoming_greeting() {
  cout << endl
       << "Automatic animal registration in progress..."
       << endl << endl;
  cout << "Please provide file name of animals you wish to send to the farm.\n"
       << "The provided file must have lines in format of (no blank entries)\n\n"
       << "\tName|Species|Breed|Service|Miscellaneous"
       << endl << endl;
}


// menu_greeting simply displays menu options; is used in menu function.
void menu_greeting() {
  cout
    << endl
    << "\t\t\t\t ╔╦╗┌─┐┌┐┌┬ ┬ \n"
    << "\t\t\t\t ║║║├┤ ││││ │ \n"
    << "\t\t\t\t ╩ ╩└─┘┘└┘└─┘ \n"
    << endl;

  cout
    << "[1] Animal Registration -- Manual\t"
    << "[2] List INCOMING farm members\n"
    << "[3] Animal Registration -- Automatic\t"
    << "[4] List CURRENT farm members \n"
    << "[5] Search current animals by species\t"
    << "[6] Search current animals by breed\n"
    << "[7] Restart\t\t\t\t"
    << "[8] Quit"
    << endl << endl;
}


// farewell displays a fun farewell message.
void farewell() {
  cout
    << endl
    << "     ╔╗ ┬ ┬┌─┐   ┬ ┬┌─┐┬  ┬┌─┐  ┌─┐  ┌┐ ┌─┐┌─┐┬ ┬┌┬┐┬┌─┐┬ ┬┬    ┌┬┐┬┌┬┐┌─┐┬\n"
    << "     ╠╩╗└┬┘├┤    ├─┤├─┤└┐┌┘├┤   ├─┤  ├┴┐├┤ ├─┤│ │ │ │├┤ │ ││     │ ││││├┤ │\n"
    << "     ╚═╝ ┴ └─┘┘  ┴ ┴┴ ┴ └┘ └─┘  ┴ ┴  └─┘└─┘┴ ┴└─┘ ┴ ┴└  └─┘┴─┘   ┴ ┴┴ ┴└─┘o\n"
    << endl;
}
