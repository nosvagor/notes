// ╔═╗┌─┐┬─┐┌─┐  ╔═╗┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// ║  │ │├┬┘├┤   ╠╣ │ │││││   │ ││ ││││└─┐
// ╚═╝└─┘┴└─└─┘  ╚  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘
// cullyn --- cs162
// Purpose: implementation of core functions of the program, does not include
// class methods, see class_implementation.cpp for those.

#include "main.h"



void read() {}



void display() {}



void edit() {}



void update() {}



void reset() {}



// ┬ ┬┌┬┐┬┬  ┬┌┬┐┬ ┬  ┌─┐┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// │ │ │ ││  │ │ └┬┘  ├┤ │ │││││   │ ││ ││││└─┐
// └─┘ ┴ ┴┴─┘┴ ┴  ┴   └  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘
//===========================================================================//

// Menu displays menu options and waits until a valid entry is given, passing
// result as an int to a switch statement.
int menu() {
  int response {0};

  menu_greeting();

  do {
    cout << "Please select a menu option: ";
    cin >> response;
    cin.clear();
    cin.ignore(420, '\n');
  } while (response < 1 || response > 8);

  return response;
}


// yes_no r
char yes_no(const char* str) {
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



void edit_update() {
  char response;
  do {
    response = yes_no("Would you like to edit any entries?");
    if (response == 'y') edit();
  } while (response != 'n');

  if (yes_no("Update current animals?") == 'y') update();
}



void call_menu (int &selection) {
  do {
    (yes_no("Return to menu? (no = quit)") == 'n') ? selection = 8 : selection = 0;
  } while (selection != 0 && selection != 8);
  if (selection == 8) farewell();
}
