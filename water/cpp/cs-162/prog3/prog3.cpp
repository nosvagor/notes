// ┌─┐┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ┌┬┐┬ ┬┬─┐┌─┐┌─┐
// ├─┘├┬┘│ ││ ┬├┬┘├─┤│││   │ ├─┤├┬┘├┤ ├┤
// ┴  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴   ┴ ┴ ┴┴└─└─┘└─┘
// cullyn newman -- cs162

// Meta-purpose: further practice using arrays of characters, but now with the
// inclusion of structures, data files, and classes.

// Program-purpose: maintain a list of animals that can perform service
// activities. Data will be organized by breed, species, service,
// compatibility, and specific (special) information that relates to each
// animal in question.
// --
// This program utilizes an external file called animal.txt that will be read
// and written to. New input taken from the user will be appended to existing
// data in file. The user will have the option to supply a different source
// file if desired instead of inputting new data.


#include <cctype>
#include <cstring>
#include <fstream>
#include <iostream>
using namespace std;

// Constants
const int N {79};   // default array size.
const int MAX {10}; // max number of animals support for manual input.

// Structs
struct animal {
  char name[N];     // custom field, name of animal.
  char species[N];  // animal species.
  char breed[N];    // if applicable, subgroup of species.
  char service[N];  // type of service the animal provides.
  char misc[N];     // other special information, specific to each animal.
} animals[MAX];     // array of structs for manual input of new animals

// Function Declarations {

// MAIN FUNCTIONS
void new_animals();   // add new animal via manual input by user.
void read_inc();      // add new animal(s) via reading from an external file.
void disp_inc();      // display list of unsaved animals.
void disp_cur();      // display main list of recorded animals.
void updt_cur();      // commit unsaved animals to main list.

// UTILITY FUNCTIONS
void greeting();               // initial greeting and instructions.
int menu();                    // recurring menu option for program navigation.
void call_menu(int &response); // return to menu
void farewell();               // exit message.

char yes_no();            // get a yes/no response.
bool confirm();           // echo and confirm input.

void reset_incoming();    // clear list of incoming animals (semi-restart)
void reset_current();     // reset list to default case (semi-restart)
bool restart();           // reset program to initial state (full-restart)
// }

//             o  o  O  O  0 0
//            ,______  ____    0
//            | MAIN \_|[]|_'__Y        PROGRAM 3! STRUCTS! EXTERNAL FILES!
//            |_______|__|_|__|} c++                                         79
//=============oo--oo==o--OOO\\================================================
int main() {

  // menu selection variable.
  int selection {0};

  greeting();

  do {
    selection = menu();
  } while (selection < 1 || selection != 6);

  return 0;
};
//=============================================================================

// ┌┬┐┌─┐┬┌┐┌  ┌─┐┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// │││├─┤││││  ├┤ │ │││││   │ ││ ││││└─┐
// ┴ ┴┴ ┴┴┘└┘  └  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘


void new_animals(){
  cout << endl << "new animals" << endl;


}

void read_inc(){
  cout << endl << "read inc" << endl;
}

void disp_inc(){
  cout << endl << "display incoming" << endl;
}

void disp_cur(){
  cout << endl << "display current" << endl;
}
void updt_cur(){
  cout << endl << "update current" << endl;
}


// ┬ ┬┌┬┐┬┬ ┌┬┐┬ ┬  ┌─┐┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// │ │ │ ││  │ └┬┘  ├┤ │ │││││   │ ││ ││││└─┐
// └─┘ ┴ ┴┴─┘┴  ┴   └  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘

char yes_no() {
  char response {};

  do {
    cin >> response;
    tolower(response);
    cin.ignore(420, '\n');
    if (response == 'n') return 'n';
  } while (response != 'y');

  return 'y';
}

void greeting() {
  cout
    << endl
    << "\t\t\t ╔═╗┌┐┌┬┌┬┐┌─┐┬    ╔═╗┌─┐┬─┐┌┬┐ \n"
    << "\t\t\t ╠═╣│││││││├─┤│    ╠╣ ├─┤├┬┘│││ \n"
    << "\t\t\t ╩ ╩┘└┘┴┴ ┴┴ ┴┴─┘  ╚  ┴ ┴┴└─┴ ┴ \n"
    << endl;

  cout
    << "Animals should be equal, free, and happy! All animals described in this program\n"
    << "have not been harmed and provide invaluable services to others that they love."
    << endl << endl;

  cout
    << "This program keep track of animals with that provide such services.\n"
    << "We do our best to make any animal at this farm feel happy and respected."
    << endl << endl;

  cout
    << "Users of this program are free to add new animals manually, or provide\n"
    << "a list of animals that wish to join the farm.\n\n"
    << "New members of our farm require a name and the service they provide to be admitted.\n"
    << "Species, breed, and other additional information may be added if desired."
    << endl << endl;

  cout
    << "Users may also simply list the animals currently in the farm.\n"
    << "Menu options will be provided to navigate the functionality of this program."
    << endl;
}

int menu() {
  int response {0};

  cout
    << endl
    << "\t\t\t\t ╔╦╗┌─┐┌┐┌┬ ┬ \n"
    << "\t\t\t\t ║║║├┤ ││││ │ \n"
    << "\t\t\t\t ╩ ╩└─┘┘└┘└─┘ \n"
    << endl;

  cout
    << "[1] Animal Registration -- Manual\t"
    << "[2] List INCOMING farm members\n"
    << "[3] Animal Registration -- Automatic\t"
    << "[4] List CURRENT farm members \n"
    << "[5] Restart\t\t\t\t"
    << "[6] Quit"
    << endl << endl;

  do {
    cout << "Please choose a menu option: ";
    cin >> response;
    cin.clear();
    cin.ignore(420, '\n');
  } while (response < 1 || response > 6);

  switch (response) {
      case 1:
        new_animals();
        call_menu(response);
        break;
      case 2:
        disp_inc();
        break;
      case 3:
        read_inc();
        break;
      case 4:
        disp_cur();
        break;
      case 5:
        cout << string(69, '\n');
        greeting();
        break;
      case 6:
        farewell();
        break;
    };
  return response;
}

void call_menu (int &response) {
  do {
    cout << "\nReturn to menu? [y/n]: ";
    (yes_no() == 'n') ? response = 6 : response = 0;
  } while (response != 0 && response != 6);
  if (response == 6) farewell();
}

void farewell() {
  cout
    << endl
    << "     ╔╗ ┬ ┬┌─┐   ┬ ┬┌─┐┬  ┬┌─┐  ┌─┐  ┌┐ ┌─┐┌─┐┬ ┬┌┬┐┬┌─┐┬ ┬┬    ┌┬┐┬┌┬┐┌─┐┬\n"
    << "     ╠╩╗└┬┘├┤    ├─┤├─┤└┐┌┘├┤   ├─┤  ├┴┐├┤ ├─┤│ │ │ │├┤ │ ││     │ ││││├┤ │\n"
    << "     ╚═╝ ┴ └─┘┘  ┴ ┴┴ ┴ └┘ └─┘  ┴ ┴  └─┘└─┘┴ ┴└─┘ ┴ ┴└  └─┘┴─┘   ┴ ┴┴ ┴└─┘o\n"
    << endl;
}
