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

// NOTES:
// Upon completing the program, I realized making two separate lists was
// probably not the best approach. Interesting exercise, but could be done
// better I suppose. I know this assignment is about creating a dynamically
// allocated array of syntax items, not a LLL, but I did this is in program 3
// and didn't want to do the exact same thing again.


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

  // I tried making this into a function, but failed... {
  // Overall, it takes data from an external and builds main list.
  ifstream in_file;
  in_file.open(CURRENT);
  syntax.build(syntax.head, syntax.tail, in_file);
  in_file.close();
  in_file.clear();
  // }

  // temporary list, updates main list via external file if desired.
  list syntax_temp;

  // basic greeting.
  greeting();

  // continue to call menu until quit option is selected.
  do {
    selection = menu(0, 9, 1);
    switch (selection) {
      //=====================================================================//
      case 1:  // DISPLAY ALL entries in MAIN list --------------------------//
        syntax.display_all(syntax.head);
        return_to_menu();
        break; // -----------------------------------------------------------//
      //=====================================================================//


      //=====================================================================//
      case 2:  // DISPLAY ALL entries in TEMPORARY list ---------------------//
        syntax_temp.display_all(syntax_temp.head);
        return_to_menu();
        break; // -----------------------------------------------------------//
      //=====================================================================//


      //=====================================================================//
      case 3:  // SEARCH MAIN list ------------------------------------------//
        // another thing I tried to make into a function, but failed. Not sure
        // how to pass a list correctly.
        {
          int search_select = 0;
          char query[SIZE];
          int matches {0};

          search_select = menu(1,2,2);

          cout << "\nSearch query: ";
          cin.get(query, SIZE, '\n');
          cin.clear();
          cin.ignore(SIZE, '\n');

          matches = syntax_temp.search(query, syntax.head, search_select);
          cout << "\nSearch complete --- total matches: " << matches << endl;
          return_to_menu();
        }
        break; // -----------------------------------------------------------//
      //=====================================================================//


      //=====================================================================//
      case 4:  // SEARCH TEMPORARY list -------------------------------------//
        // Same thing as case 3, but takes into account temp list might be
        // empty.
        if (!syntax_temp.head) {
          cout << "\nWARNING: nothing to search." << endl;
          return_to_menu();
          break;
        }

        {
          int search_select = 0;
          char query[SIZE];
          int matches {0};

          search_select = menu(1,2,2);

          cout << "\nSearch query: ";
          cin.get(query, SIZE, '\n');
          cin.clear();
          cin.ignore(SIZE, '\n');

          matches = syntax_temp.search(query, syntax_temp.head, search_select);
          cout << "\nSearch complete --- total matches: " << matches << endl;
          return_to_menu();
        }
        break; // -----------------------------------------------------------//
      //=====================================================================//


      //=====================================================================//
      case 5:  // EDIT an entry in MAIN list --------------------------------//
        // Another placed where inability to pass list as argument in function
        // failed me. Cases 5 and 6 are essentially the same, but for different
        // LLL.
        do {
          if (!syntax.head) {
            cout << "\nWARNING: nothing to edit." << endl;
            break;
          }

          char name[SIZE];
          int matches {0};

          cout << "\nName of entry to edit: ";
          cin.get(name, SIZE, '\n');
          cin.clear();
          cin.ignore(SIZE, '\n');

          matches = syntax.search(name, syntax.head, 1);

          if (matches == 0) {
            cout << "\nWARNING: no match found." << endl;
            break;
          }

          if (matches > 1)
            cout << "\nWARNING: duplicate matches. Editing first match."
                 << endl;

          syntax.edit(name, syntax.head);
          cout << "\nEdit complete! --- ";
        } while (yes_no("Edit another entry?"));

        return_to_menu();
        break; // -----------------------------------------------------------//
        //=====================================================================//


      //=====================================================================//
      case 6:  // EDIT an entry in TEMPORARY list ---------------------------//
        // Same as case 5, but for temporary list.
        do {
          if (!syntax_temp.head) {
            cout << "\nWARNING: nothing to edit." << endl;
            break;
          }

          char name[SIZE];
          int matches {0};

          cout << "\nName of entry to edit: ";
          cin.get(name, SIZE, '\n');
          cin.clear();
          cin.ignore(SIZE, '\n');

          matches = syntax_temp.search(name, syntax_temp.head, 1);

          if (matches == 0) {
            cout << "\nWARNING: no match found." << endl;
            break;
          }

          if (matches > 1)
            cout << "\nWARNING: duplicate matches. Editing first match."
                 << endl;

          syntax_temp.edit(name, syntax_temp.head);
          cout << "\nEdit complete! --- ";
        } while (yes_no("Edit another entry?"));

        return_to_menu();
        break; // -----------------------------------------------------------//
      //=====================================================================//


      //=====================================================================//
      case 7:  // UPDATE MAIN list with temporary list ----------------------//
        if (!syntax_temp.head) {
          cout << "\nWARNING: nothing to add." << endl;
          return_to_menu();
          break;
        }

        // write temporary list to external file (CURRENT) then reset {
        save(syntax_temp.head);
        syntax_temp.destroy(syntax_temp.head);
        syntax_temp.~list();
        new (& syntax_temp) list;
        // }

        // reset main list with newly updated data from external file {
        syntax.destroy(syntax.head);
        syntax.~list();
        new (& syntax) list;

        in_file.open(CURRENT);
        syntax.build(syntax.head, syntax.tail, in_file);
        in_file.close();
        in_file.clear();
        // }

        if (yes_no("\nNew entries written to file. Display updated list?"))
          syntax.display_all(syntax.head);

        return_to_menu();
        break; // -----------------------------------------------------------//
      //=====================================================================//


      //=====================================================================//
      case 8:  // UPDATE TEMP list with new input (manual or auto) ----------//

        cout << endl;
        if (yes_no("Manual entry?")) {
          // insert new entry at end of LLL
          syntax_temp.insert(syntax_temp.head);
        } else {

          // string used for path to supplied external file.. if used.
          char file_path[SIZE];
          ifstream in_file;

          // loads an external example file, simulating new data entries.
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

          // build new list once file is opened and valid
          syntax_temp.build(syntax_temp.head, syntax_temp.tail, in_file);
          in_file.close();
          in_file.clear();
        }

        cout << endl;
        if (yes_no("New entries added; display new entries list now?"))
          syntax_temp.display_all(syntax_temp.head);

        return_to_menu();
        break; // -----------------------------------------------------------//
      //=====================================================================//


      //=====================================================================//
      case 9:  // RESET -----------------------------------------------------//

        //reset temp file {
        syntax_temp.destroy(syntax_temp.head);
        syntax_temp.~list();
        new (& syntax_temp) list;
        // }

        // self explanatory...
        if (yes_no("\nReset current file with original list?")) {

          file_reset();
          syntax.destroy(syntax.head);
          syntax.~list();
          new (& syntax) list;

          in_file.open(CURRENT);
          syntax.build(syntax.head, syntax.tail, in_file);
          in_file.close();
          in_file.clear();
        }

        cout << "\nRequested files reset." << endl;

        return_to_menu();
        break; // -----------------------------------------------------------//
      //=====================================================================//


      //=====================================================================//
      case 0:  // QUIT ------------------------------------------------------//
        if (syntax_temp.head) {
          cout << "\nWARNING: unsaved entries.\n" << endl;

          if (yes_no("Update current file with new entries?")) {
            save(syntax_temp.head);
            cout << "\nFiles updated!" << endl;

            // delete allocated memory... Is this necessary?
            syntax_temp.destroy(syntax_temp.head);
            syntax_temp.~list();
            syntax.destroy(syntax.head);
            syntax.~list();
          }
        }
        break; // -----------------------------------------------------------//
      //=====================================================================//
    };
  } while (selection != 0);

  farewell();

  return 0;
};
