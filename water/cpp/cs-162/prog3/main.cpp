// ╔╦╗┌─┐┬┌┐┌
// ║║║├─┤││││
// ╩ ╩┴ ┴┴┘└┘
// cullyn --- cs162
// Purpose: maintain a list of animals that can perform service activities.
// Data will be organized by breed, species, service, compatibility, and
// other specific information that relates to each animal in question.
//
// A menu with other options will be available that provides additional
// functionality, including loading new animals from external files, searching
// by breed or species.

#include "main.h"

//             o  o  O  O  0 0
//            ,______  ____    0
//            | MAIN \_|[]|_'__Y
//            |_______|__|_|__|} c++                                         79
//=============oo--oo==o--OOO\\================================================
int main() {

  // menu selection variable.
  int selection {0};

  greeting();

  do {
    selection = menu();
    switch (selection) {
      case 1:
        cout << "1 selected" << endl;
        break;
      case 2:
        cout << "2 selected" << endl;
        break;
      case 3:
        cout << "3 selected" << endl;
        break;
      case 4:
        cout << "4 selected" << endl;
        break;
      case 5:
        cout << "5 selected" << endl;
        break;
      case 6:
        cout << "6 selected" << endl;
        break;
      case 7:
        cout << "7 selected" << endl;
        break;
      case 8:
        cout << "8 selected" << endl;
        break;
    };
  } while (selection < 1 || selection != 8);

  farewell();

  return 0;
};
