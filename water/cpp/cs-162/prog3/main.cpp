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
  int incoming_count {0};

  greeting();

  // do {
  //   selection = menu();
  //   switch (selection) {
  //     case 1:
  //       reset_incoming();
  //       new_animals();
  //       incoming_count = disp_inc();
  //       call_edit(incoming_count);
  //       break;
  //     case 2:
  //       if (animals[0].name[0] == 0) {
  //         cout << "\nNo incoming animals, returning to menu..." << endl << endl;
  //         this_thread::sleep_for(chrono::milliseconds(1500));
  //       } else {
  //         inc_count = disp_inc();
  //         call_edit(inc_count);
  //       };
  //       break;
  //     case 3:
  //       reset_incoming();
  //       read_inc(inc_count);
  //       call_edit(inc_count);
  //       break;
  //     case 4:
  //       disp_cur();
  //       call_menu(selection);
  //       break;
  //     case 5:
  //       break;
  //     case 6:
  //       break;
  //     case 7:
  //       reset_current();
  //       cout << string(69*2, '\n');
  //       greeting();
  //       break;
  //     case 8:
  //       reset_current();
  //       farewell();
  //       break;
  //   };
  // } while (selection < 1 || selection != 8);

  farewell();

  return 0;
};
