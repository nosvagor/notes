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

  animals incoming;
  animals current;

  greeting();

  do {
    selection = menu();
    switch (selection) {
      case 1:  // Manual animal registration.
        incoming.read_all();
        break;
      case 2:  // Display INCOMING animals.
        incoming.display_all();
        if (incoming.animal_count > 0) update(current);
        break;
      case 3:  // Automatic animal registration.
        incoming.read_all_auto();
        break;
      case 4:  // Display CURRENT animals.
        current.read_file_only();
        current.display_all();
        break;
      case 5:  // Search animals by species.
        break;
      case 6:  // Search animals by breed.
        break;
      case 7:  // Restart program.
        break;
      case 8:  // Quit program.
        break;
    };
  } while (selection < 1 || selection != 8);

  farewell();

  return 0;
};
