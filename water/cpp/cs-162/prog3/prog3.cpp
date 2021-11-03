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
#include <chrono>
#include <thread>
using namespace std;

// Constants
const int N {69};      // default array size.
const int MAX {2};     // max number of animals support for manual input.

const char *CUR_ANIMALS = "animals.txt";    // main data file
const char DLM = '|';                       // delimiter used when parsing file

// Structure
struct animal {
  char name[N];     // custom field, name of animal.
  char species[N];  // animal species.
  char breed[N];    // if applicable, subgroup of species.
  char service[N];  // type of service the animal provides.
  char misc[2*N];   // other special information, specific to each animal.
} animals[MAX-1],           // for input of new animals.
  animals_all[(2*MAX)-1];   // new animals and/or current list of animals.

// Function Declarations {
// MAIN FUNCTIONS
void new_animals();   // add new animal via manual input by user.
void read_inc();      // add new animal(s) via reading from an external file.
void disp_inc();      // display list of unsaved animals (animals array).

void read_cur();      // read in current members from external file.
void updt_cur();      // write unsaved animals to main list
void disp_all();      // update and display main list of recorded animals.

// UTILITY FUNCTIONS
void greeting();               // initial greeting and instructions.
int menu();                    // recurring menu option for program navigation.
void call_menu(int &response); // return to menu
void farewell();               // exit message.

void reset_struct();           // resets stricture.
char yes_no(const char* str);  // get a yes/no response.
bool confirm();                // echo and confirm input.

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


void new_animals() {
  char response {'y'};

  cout << "Adding new farm members... " << endl << endl;

  for (int i = 0; i < MAX && response == 'y'; i++) {
    cout << "Name: ";
    cin >> animals[i].name;
    cout << "Species: ";
    cin >> animals[i].species;
    cout << "Breed: ";
    cin >> animals[i].breed;
    cout << "Service: ";
    cin >> animals[i].service;
    cout << "Misc: ";
    cin >> animals[i].misc;
    cout << endl;

    if (!(i+1 == MAX)) {
      do {
        (yes_no("Add another?") == 'n') ? response = 'n' : response = 'y';
      } while (!(response == 'y' || response == 'n'));
    } else if (i+1 == MAX) {
      cout << "Max number new animals reached for manual input... Echoing input..." << endl;
      this_thread::sleep_for(chrono::milliseconds(1500));
    };
  };
}

void read_inc(){
  char new_animals[N];
  int i {0};

  cout << endl
       << "Automatic animal registration in progress..."
       << endl << endl;
  cout << "Please provide file name of animals you wish to send to the farm.\n"
       << "\t E.g., example_list.txt is provided for demonstration of automatic entries. \n\n"
       << "The Provided file must have lines in format of\n\n"
       << "\tName|Species|Breed|Service|Miscellaneous\n\n"
       << "Please enter \"none\" if these is no extra info associated with the animal,\n"
       << "and \"unsure\" for data for other entries."
       << endl << endl;

  cout << "File name: ";
  cin.get(new_animals, N, '\n');
  cin.ignore(420, '\n');

  ifstream in_file;

  in_file.open(new_animals);

  while (in_file && !in_file.eof() && i < MAX) {
    in_file.get(animals[i].name, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals[i].species, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals[i].breed, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals[i].service, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals[i].misc, N, '\n');
    in_file.ignore(100, '\n');

    ++i;
  };

  disp_inc();

  if (i >= MAX) {
    cout << "!! Attention !! --- New animal registration can only support "
         << MAX << " animals at once.\nOnly the first "
         << MAX << " made it in."
         << endl << endl;
  };

  in_file.close();
  in_file.clear();
}

void disp_inc(){
  cout << endl << "Displaying incoming farm animals:" << endl << endl;

  for (int i = 0; i < MAX; i++) {
    if (!(animals[i].name[0] == 0)) {
      cout << "Name: "
        << animals[i].name << "\n";
      cout << "  - Species: "
        << animals[i].species << "\n";
      cout << "  - Breed: "
        << animals[i].breed << "\n";
      cout << "  - Service: "
        << animals[i].service << "\n";
      cout << "  - Misc: "
        << animals[i].misc << "\n" << endl;
    };
  };
}

void disp_cur(){
  cout << endl << "Displaying current..." << endl << endl;

  int i {0};

  ifstream in_file;

  in_file.open(CUR_ANIMALS);

  while (in_file && !in_file.eof() && i < 2*MAX) {
    in_file.get(animals_all[i].name, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals_all[i].species, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals_all[i].breed, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals_all[i].service, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals_all[i].misc, N, '\n');
    in_file.ignore(100, '\n');

    ++i;
  };

  for (int i = 0; i < 2*MAX; i++) {
    if (!(animals_all[i].name[0] == 0)) {
      cout << "Name: "
           << animals_all[i].name << "\n";
      cout << "  - Species: "
           << animals_all[i].species << "\n";
      cout << "  - Breed: "
           << animals_all[i].breed << "\n";
      cout << "  - Service: "
           << animals_all[i].service << "\n";
      cout << "  - Misc: "
           << animals_all[i].misc << "\n"
           << endl;
    };
  };

  if (i >= 2*MAX) {
    cout << "!! Attention !! --- Farm at capacity! Only the first "
         << 2*MAX << " made it in!"
         << endl << endl;
  };

  in_file.close();
  in_file.clear();

}

void updt_cur(){
  cout << endl << "update current" << endl;


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
        reset_struct();
        new_animals();
        disp_inc();
        response = yes_no("Would you like to edit any entries?");
        if (response == 'y') cout << "yes edit" << endl;
        break;
      case 2:
        if (animals[0].name[0] == 0) {
          cout << "\nNo incoming animals, returning to menu..." << endl << endl;
          this_thread::sleep_for(chrono::milliseconds(1500));
        } else {
          disp_inc();
          call_menu(response);
        }
        break;
      case 3:
        read_inc();
        call_menu(response);
        break;
      case 4:
        disp_cur();
        call_menu(response);
        break;
      case 5:
        cout << string(69, '\n');
        reset_struct();
        greeting();
        break;
      case 6:
        farewell();
        break;
  };
  return response;
}


// ┬ ┬┌┬┐┬┬ ┌┬┐┬ ┬  ┌─┐┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// │ │ │ ││  │ └┬┘  ├┤ │ │││││   │ ││ ││││└─┐
// └─┘ ┴ ┴┴─┘┴  ┴   └  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘

void reset_struct() {
  memset(animals, 0, sizeof(animals));
  animals[MAX-1] = animal();
}

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

void call_menu (int &response) {
  do {
    (yes_no("Return to menu? (no = quit)") == 'n') ? response = 6 : response = 0;
  } while (response != 0 && response != 6);
  if (response == 6) farewell();
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
    << "\t Max number of new animals: "<< MAX << "\n"
    << "\t Max number of total animals: " << 2*MAX << "\n\n"
    << "New members of our farm require a name, species, breed, service they \n"
    << "provide to be admitted; other additional information may be added if desired."
    << endl << endl;

  cout
    << "Users may also simply list the animals currently in the farm.\n"
    << "Menu options will be provided to navigate the functionality of this program."
    << endl;
}

void farewell() {
  cout
    << endl
    << "     ╔╗ ┬ ┬┌─┐   ┬ ┬┌─┐┬  ┬┌─┐  ┌─┐  ┌┐ ┌─┐┌─┐┬ ┬┌┬┐┬┌─┐┬ ┬┬    ┌┬┐┬┌┬┐┌─┐┬\n"
    << "     ╠╩╗└┬┘├┤    ├─┤├─┤└┐┌┘├┤   ├─┤  ├┴┐├┤ ├─┤│ │ │ │├┤ │ ││     │ ││││├┤ │\n"
    << "     ╚═╝ ┴ └─┘┘  ┴ ┴┴ ┴ └┘ └─┘  ┴ ┴  └─┘└─┘┴ ┴└─┘ ┴ ┴└  └─┘┴─┘   ┴ ┴┴ ┴└─┘o\n"
    << endl;
}
