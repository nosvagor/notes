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

  int selection {0};  // menu selection variable.
  animals incoming;   // object of objects, for new animals
  animals current;    // object of objects, for existing animals.

  current.read_file_only();

  greeting();

  // continue to call menu until quit.
  do {
    selection = menu();
    switch (selection) {
      case 1:  // Manual animal registration.
        incoming.read_all();
        break;
      case 2:  // Display INCOMING animals.
        bool reset;
        incoming.display_all();

        if (incoming.animal_count > 0) {
          reset = incoming.call_update();
        } else {
          cout << "\nNo incoming animals, please register new animals." << endl;
          return_to_menu();
        }

        // reset incoming animals object is is right way.
        if (reset) {
          incoming.~animals();      // call destructor
          new (&incoming) animals;  // call constructor again.
        }
        break;
      case 3:  // Automatic animal registration.
        incoming.read_all_auto();
        break;
      case 4:  // Display CURRENT animals.
        current.~animals();
        new (&current) animals;
        current.read_file_only();
        current.display_all();
        cout << "\nAll current farm animals listed." << endl;
        return_to_menu();
        break;
      case 5:  // Search animals by species.
        current.display_all();
        current.call_compare("species");
        return_to_menu();
        break;
      case 6:  // Search animals by breed.
        current.display_all();
        current.call_compare("breed");
        return_to_menu();
        break;
      case 7:  // Restart program.
        // always reset incoming on restart
        incoming.~animals();
        new (&incoming) animals;

        file_reset();
        break;
      case 8:  // Quit program.
        file_reset();
        break;
    };
  } while (selection < 1 || selection != 8);

  farewell();

  return 0;
};
