// ╔╦╗┌─┐┬┌┐┌
// ║║║├─┤││││
// ╩ ╩┴ ┴┴┘└┘
// cullyn --- cs162 --- program 4
// Purpose: file containing int main(). Switch statement used for menu options
// that will allow user to navigate the program. Initial list of syntax entries
// will be built from an external file, and stored as a linear linked list of
// individual class objects that will contain data about each syntax item.

// A temporary list can be updated with manual user input, or from an external
// file. This temporary list will update the main list if desired, which will
// write data to the external file that is used to build the main list.


//             o  o  O  O  0 0
//            ,______  ____    0
//            | MAIN \_|[]|_'__Y
//            |_______|__|_|__|} c++                                         79
//=============oo--oo==o--OOO\\================================================
                                                #include "header.h"
//=============================================================================
int main() {

  // menu selection variable.
  int selection {0};

  // main list, from data from file
  // list syntax;
  // syntax.build();

  // // temporary list, updates main list via external file if desired.
  // list syntax_temp;

  greeting();

  // continue to call menu until quit option is selected.
  do {
    selection = menu();
    switch (selection) {
      //=====================================================================//
      case 1:  // DISPLAY ALL entries in MAIN list --------------------------//
        break;
      //=====================================================================//

      //=====================================================================//
      case 2:  // DISPLAY ALL entries in TEMPORARY list ---------------------//
        break;
      //=====================================================================//

      //=====================================================================//
      case 3:  // SEARCH MAIN list ------------------------------------------//
        break;
      //=====================================================================//

      //=====================================================================//
      case 4:  // SEARCH TEMPORARY list -------------------------------------//
        break;
      //=====================================================================//

      //=====================================================================//
      case 5:  // EDIT an entry in MAIN list --------------------------------//
        break;
      //=====================================================================//

      //=====================================================================//
      case 6:  // EDIT an entry in TEMPORARY list ---------------------------//
        break;
      //=====================================================================//

      //=====================================================================//
      case 7:  // UPDATE MAIN list with temporary list ----------------------//
        break;
      //=====================================================================//

      //=====================================================================//
      case 8:  // UPDATE TEMP list with new input (manual or auto) ----------//
        break;
      //=====================================================================//

      //=====================================================================//
      case 9:  // RESET -----------------------------------------------------//
        break;
      //=====================================================================//

      //=====================================================================//
      case 0:  // QUIT ------------------------------------------------------//
        break;
      //=====================================================================//
    };
  } while (selection != 0);

  farewell();

  return 0;
};
