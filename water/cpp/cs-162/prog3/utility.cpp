// ╦ ╦┌┬┐┬┬  ┬┌┬┐┬ ┬  ╔═╗┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// ║ ║ │ ││  │ │ └┬┘  ╠╣ │ │││││   │ ││ ││││└─┐
// ╚═╝ ┴ ┴┴─┘┴ ┴  ┴   ╚  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘
// cullyn cs162
// Purpose: this file contains various small utility functions used within
// several other core functions.

#include "main.h"

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

