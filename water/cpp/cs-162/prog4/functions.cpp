// ┌─┐┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// ├┤ │ │││││   │ ││ ││││└─┐
// └  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘
// cullyn --- cs162 --- program 4
// Purpose: implementation of core functions of the program, does not include
// class methods, see classes.cpp.

//===========================================================================//
  #include "header.h"
//===========================================================================//

// menu displays menu options and waits until a valid entry is given, passing
// result as an int to a switch statement.
int menu() {
  int selection {-1};

  menu_greeting();

  do {
    cout << "Please select a menu option: ";
    cin >> selection;
    cin.clear();
    cin.ignore(420, '\n');
  } while (selection < 0 || selection > 9);

  return selection;
}



// yes_no is a confirmation function that takes in a custom array
// of characters and returns response char; more idiomatic than boolean.
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



// file_reset takes the original data provided and overwrites any appended
// content to the main working file, effectively resetting program data.
void file_reset() {
  if (yes_no("\nReset current animal list?") == 'y') {

    // local variables
    int N = 512;        // line size, large just in case.
    ifstream in_file;   // in file, most cases: src/original.txt
    ofstream out_file;  // out file, most cases: src/current.txt

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
    << "\t\t  ┌─┐┬ ┬┌┐┌┌┬┐┌─┐─┐ ┬  ┬─┐┌─┐┬  ┬┬┌─┐┬ ┬ \n"
    << "\t\t  └─┐└┬┘│││ │ ├─┤┌┴┬┘  ├┬┘├┤ └┐┌┘│├┤ │││ \n"
    << "\t\t  └─┘ ┴ ┘└┘ ┴ ┴ ┴┴ └─  ┴└─└─┘ └┘ ┴└─┘└┴┘ \n"
    << endl;

  cout
    << "This program keep track of useful syntax, providing a short description,\n"
    << " example, difficulty level (1--5), and whether or not you've used it.\n"
    << endl;

  cout
    << "Menu options will be provided to navigate the functionality of this program.\n"
    << "Further prompts may be provided, depending on selection."
    << endl;
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
    << "[1] DISPLAY existing syntax entries\t"
    << "[2] DISPLAY new syntax entries\n"
    << "[3] SEARCH existing syntax entries\t"
    << "[4] SEARCH new syntax entries \n"
    << "[5] EDIT an existing syntax entry\t"
    << "[6] EDIT a new syntax entry\n"
    << "[7] UPDATE existing with new entries\t"
    << "[8] UPDATE new entries (manual or auto)\n"
    << "[9] Reset\t\t\t\t"
    << "[0] Quit\n"
    << endl;
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
