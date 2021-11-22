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

  // main list, constructed using data from file
  list syntax;

  ifstream in_file;
  in_file.open(CURRENT);
  syntax.build(syntax.head, syntax.tail, in_file);
  in_file.close();
  in_file.clear();

  // temporary list, updates main list via external file if desired.
  list syntax_temp;

  greeting();

  // continue to call menu until quit option is selected.
  do {
    selection = menu();
    switch (selection) {
      //=====================================================================//
      case 1:  // DISPLAY ALL entries in MAIN list --------------------------//
        syntax.display_all(syntax.head);
        return_to_menu();
        break;
      //=====================================================================//
      //=====================================================================//
      case 2:  // DISPLAY ALL entries in TEMPORARY list ---------------------//
        syntax_temp.display_all(syntax_temp.head);
        return_to_menu();
        break;
      //=====================================================================//

      //=====================================================================//
      case 3:  // SEARCH MAIN list ------------------------------------------//
        return_to_menu();
        break;
      //=====================================================================//

      //=====================================================================//
      case 4:  // SEARCH TEMPORARY list -------------------------------------//
        return_to_menu();
        break;
      //=====================================================================//

      //=====================================================================//
      case 5:  // EDIT an entry in MAIN list --------------------------------//
        return_to_menu();
        break;
      //=====================================================================//

      //=====================================================================//
      case 6:  // EDIT an entry in TEMPORARY list ---------------------------//
        return_to_menu();
        break;
      //=====================================================================//

      //=====================================================================//
      case 7:  // UPDATE MAIN list with temporary list ----------------------//
        if (!syntax_temp.head) {
          cout << "\nWARNING: nothing to add." << endl;
          return_to_menu();
          break;
        }

        save(syntax_temp.head);
        syntax_temp.destroy(syntax_temp.head);
        syntax_temp.~list();
        new (& syntax_temp) list;

        syntax.destroy(syntax.head);
        syntax.~list();
        new (& syntax) list;

        in_file.open(CURRENT);
        syntax.build(syntax.head, syntax.tail, in_file);
        in_file.close();
        in_file.clear();

        if (yes_no("\nNew entries written to file. Display updated list?"))
          syntax.display_all(syntax.head);

        return_to_menu();
        break;
      //=====================================================================//

      //=====================================================================//
      case 8:  // UPDATE TEMP list with new input (manual or auto) ----------//

        cout << endl;
        if (yes_no("Manual entry?")) {
          syntax_temp.insert(syntax_temp.head);
        } else {

          char file_path[SIZE];
          ifstream in_file;

          cout << endl;
          if (yes_no("Automatic entry: use example file?")) {
            in_file.open(EXAMPLE);
          } else {
            cout << "File path: ";
            cin.get(file_path, SIZE, '\n');
            cin.clear();
            cin.ignore(SIZE, '\n');
            in_file.open(file_path);

            if (!in_file) {
              cout << "WARNING: Unable to read file." << endl;
              return_to_menu();
              break;
            }
          }

          syntax_temp.build(syntax_temp.head, syntax_temp.tail, in_file);
          in_file.close();
          in_file.clear();
        }

        if (yes_no("\nNew entries added; display new entries list now?"))
          syntax_temp.display_all(syntax_temp.head);

        return_to_menu();
        break;
      //=====================================================================//

      //=====================================================================//
      case 9:  // RESET -----------------------------------------------------//
        save(syntax_temp.head);
        syntax_temp.destroy(syntax_temp.head);
        syntax_temp.~list();
        new (& syntax_temp) list;

        if (yes_no("\nReset current file with original list?"))
          file_reset();

        cout << "\nRequested files reset." << endl;

        return_to_menu();
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
